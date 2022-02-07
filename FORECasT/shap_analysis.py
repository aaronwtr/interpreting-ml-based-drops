import pandas as pd
import numpy as np
from shap import KernelExplainer
import subprocess
import os
import io
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

from predictor.features import calculateFeaturesForGenIndelFile, readFeaturesData
from predictor.model import readTheta, computePredictedProfile
from predictor.predict import DEFAULT_MODEL, predictMutations, INDELGENTARGET_EXE, fetchRepReads
from selftarget.indel import tokFullIndel
from selftarget.profile import fetchIndelSizeCounts
from selftarget.view import plotProfiles

'''
In this script, the FORECasT pre-trained model is implemented and SHAP analysis is consequently performed on top of this
implementation.
'''


def getProfileCounts(profile):
    total = sum([profile[x] for x in profile])
    if total == 0:
        return []
    indel_total = total
    if '-' in profile:
        indel_total -= profile['-']
        null_perc = profile['-'] * 100.0 / indel_total if indel_total != 0 else 100.0
        null_profile = (profile['-'], '-', profile['-'] * 100.0 / total, null_perc)
    counts = [(profile[x], x, profile[x] * 100.0 / total, profile[x] * 100.0 / indel_total) for x in profile if
              x != '-']
    counts.sort(reverse=True)
    if '-' in profile:
        counts = [null_profile] + counts
    return counts


def writePredictedProfileToSummary(p1, fout):
    counts = getProfileCounts(p1)
    for cnt, indel, _, _ in counts:
        if cnt < 0.5: break
        fout.write(u'%s\t-\t%d\n' % (indel, np.round(cnt)))


def writePredictedRepReadsToFile(p1, rep_reads, fout):
    counts = getProfileCounts(p1)
    idx = 0
    for cnt, indel, _, _ in counts:
        if cnt < 0.5: break
        fout.write(u'%d\t%s\t%s\n' % (idx, rep_reads[indel], indel))
        idx += 1


def writeProfilesToFile(out_prefix, profiles_and_rr, write_rr=False):
    fout = io.open(out_prefix + '_predictedindelsummary.txt', 'w')
    if write_rr: fout_rr = io.open(out_prefix + '_predictedreads.txt', 'w')
    for (guide_id, prof, rep_reads, in_frame) in profiles_and_rr:
        if len(profiles_and_rr) > 1:
            id_str = u'@@@%s\t%.3f\n' % (guide_id, in_frame)
            fout.write(id_str)
            if write_rr:
                fout_rr.write(id_str)
        writePredictedProfileToSummary(prof, fout)
        if write_rr:
            writePredictedRepReadsToFile(prof, rep_reads, fout_rr)
    fout.close()


def predictMutationsSingle(target_seq, pam_idx, out_prefix, theta_file=DEFAULT_MODEL):
    print('Predicting mutations...')
    p_predict, rep_reads, in_frame_perc = predictMutations(theta_file, target_seq, pam_idx)
    print('Writing to file...')
    writeProfilesToFile(out_prefix, [('Test Guide', p_predict, rep_reads, in_frame_perc)], write_rr=True)
    print('Done!')


def predictMutations(theta_file, target_seq, pam_idx, add_null=True):
    theta, train_set, theta_feature_columns = readTheta(theta_file)

    # generate indels
    left_trim = 0
    tmp_genindels_file = 'tmp_genindels_%s_%d.txt' % (target_seq, random.randint(0, 100000))
    cmd = INDELGENTARGET_EXE + ' %s %d %s' % (target_seq, pam_idx, tmp_genindels_file)
    print(cmd)
    subprocess.check_call(cmd.split())
    rep_reads = fetchRepReads(tmp_genindels_file)
    isize, smallest_indel = min([(tokFullIndel(x)[1], x) for x in rep_reads]) if len(rep_reads) > 0 else (0, '-')
    if isize > 0: left_trim = target_seq.find(rep_reads[smallest_indel][:10])

    # compute features for all generated indels
    tmp_features_file = 'tmp_features_%s_%d.txt' % (target_seq, random.randint(0, 100000))
    calculateFeaturesForGenIndelFile(tmp_genindels_file, target_seq, pam_idx - 3, tmp_features_file)
    os.remove(tmp_genindels_file)
    feature_data, feature_columns = readFeaturesData(tmp_features_file)
    os.remove(tmp_features_file)

    if len(set(theta_feature_columns).difference(set(feature_columns))) != 0:
        raise Exception('Stored feature names associated with model thetas are not contained in those computed')

    if len(set(theta_feature_columns).union(set(feature_columns))) != len(theta_feature_columns):
        feature_data = feature_data[['Indel'] + theta_feature_columns]
        feature_columns = theta_feature_columns

    # Predict the profile
    p_predict, _ = computePredictedProfile(feature_data, theta, theta_feature_columns)
    in_frame, out_frame, _ = fetchIndelSizeCounts(p_predict)
    in_frame_perc = in_frame * 100.0 / (in_frame + out_frame)
    if add_null:
        p_predict['-'] = 1000
        rep_reads['-'] = target_seq[left_trim:]
    return p_predict, rep_reads, in_frame_perc


def getSHAPValue(model, feature_data, link='logit'):
    explainer = KernelExplainer(model, feature_data, link=link)
    shap_value = explainer.shap_values(feature_data)

    return shap_value


if __name__ == '__main__':
    # Note that not all oligo's in the guideset are present in the Tijsterman data present locally.
    guideset = pd.read_csv("FORECasT/guideset_data.txt", sep='\t')
    target_seq = guideset['TargetSequence'][19]  # second index indicates oligo under inspection. if we want to consider
                                                # all oligo's, make for loop.
    pam_idx = guideset['PAM Index'][19]
    feature_data = pd.read_pickle("FORECasT/train/Tijsterman_Analyser/" + str(guideset['ID'][19][0:5]) + '_' + str(guideset['ID'][19][5:]))
    small_feature_data = feature_data.iloc[0:5, 0:5]

    profile, rep_reads, in_frame = predictMutations(DEFAULT_MODEL, target_seq, pam_idx)
    plotProfiles([profile], [rep_reads], [pam_idx], [False], ['Predicted'], title='In Frame: %.1f%%' % in_frame)
    # plt.show()


    shap_value = tqdm(getSHAPValue(predictMutations(DEFAULT_MODEL, target_seq, pam_idx), small_feature_data))

    print(shap_value)