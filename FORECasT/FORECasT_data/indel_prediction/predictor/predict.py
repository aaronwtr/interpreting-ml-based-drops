import io, os, csv, sys, re, random, itertools, subprocess
import numpy as np
import pylab as PL
import Bio.Seq
import pandas as pd

from selftarget.profile import fetchIndelSizeCounts, getProfileCounts

from selftarget.view import plotProfiles
from selftarget.plot import setFigType
from selftarget.util import setPlotDir, getIndelGenExe, setIndelGenExe
from selftarget.indel import tokFullIndel

from predictor.model import computePredictedProfile, readTheta, setFeaturesDir, setReadsDir
from predictor.features import calculateFeaturesForGenIndelFile, readFeaturesData

REPO_PATH = "C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/interpreting-ml-based-drops/FORECasT/"
INDELGENTARGET_EXE = os.getenv("INDELGENTARGET_EXE",
                               str(REPO_PATH) + "FORECasT_data/indel_analysis/indelmap/build/indelgentarget.exe")
DEFAULT_MODEL = "FORECasT/FORECasT_data/indel_prediction/predictor/forecast_pre_trained_model.txt"


def setIndelGenTargetExeLoc(val):
    global INDELGENTARGET_EXE
    INDELGENTARGET_EXE = val


def fetchRepReads(genindels_file):
    f = io.open(genindels_file)
    rep_reads = {toks[0]: toks[-1] for toks in csv.reader(f, delimiter='\t') if 'Git' not in toks[0]}
    f.close()
    return rep_reads


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


def predictMutations(theta_file, target_seq, pam_idx, add_null=True):
    theta, train_set, theta_feature_columns = readTheta(theta_file)

    # generate indels
    left_trim = 0
    tmp_genindels_file = 'tmp_genindels_%s_%d.txt' % (target_seq, random.randint(0, 100000))
    cmd = INDELGENTARGET_EXE + ' %s %d %s' % (target_seq, pam_idx, tmp_genindels_file)
    print(cmd);
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


def plot_predictions(theta_file, target_seq, pam_idx):
    if pam_idx < 0 or pam_idx >= (len(target_seq) - 3):
        raise Exception('PAM idx out of range')

    if sum([x in ['A', 'T', 'G', 'C'] for x in target_seq]) != len(target_seq):
        raise Exception('Sequence must be composed of A,T,G,or C only')

    if len(target_seq) < 20 or pam_idx < 13 or pam_idx > len(target_seq) - 7:
        raise Exception(
            'Sequence too short or PAM too close to edge of sequence (must have at least 10nt either side of cut site)')

    if target_seq[pam_idx + 1:pam_idx + 3] != 'GG':
        raise Exception('Non NGG PAM (check correct index of PAM)')

    profile, rep_reads, in_frame = predictMutations(theta_file, target_seq, pam_idx)
    out_filename = '%s_%d.txt' % (target_seq, pam_idx)
    fout = io.open(out_filename, 'w')
    fout.write(u'@@@%s\n' % ('%.1f' % in_frame))
    writePredictedProfileToSummary(profile, fout)
    fout.close()
    setFigType('png')
    fig = plotProfiles([profile], [rep_reads], [pam_idx], [False], ['Predicted'], title='In Frame: %.1f%%' % in_frame)
    return fig


def predictProfilesBulk(theta_file, target_file):
    # Target File: a tab-delimited file with columns:  ID, Target, PAM Index
    profiles_and_rr = []
    f = io.open(target_file)
    for row in csv.DictReader(f, delimiter='\t'):
        prof, rep_reads, in_frame = predictMutations(theta_file, row['Target'], eval(row['PAM Index']))
        profiles_and_rr.append((row['ID'], prof, rep_reads, in_frame))
    f.close()
    return profiles_and_rr


def writeProfilesToFile(out_prefix, profiles_and_rr, write_rr=False):
    fout = io.open(out_prefix + '_predictedindelsummary.txt', 'w')
    if write_rr: fout_rr = io.open(out_prefix + '_predictedreads.txt', 'w')
    for (guide_id, prof, rep_reads, in_frame) in profiles_and_rr:
        if len(profiles_and_rr) > 1:
            id_str = u'@@@%s\n' % guide_id
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


def predictMutationsBulk(target_file, out_prefix, theta_file=DEFAULT_MODEL):
    # Target File: a tab-delimited file with columns:  ID, Target, PAM Index
    print('Predicting mutations...')
    profiles_and_rr = predictProfilesBulk(theta_file, target_file)
    print('Writing to file...')
    writeProfilesToFile(out_prefix, profiles_and_rr, write_rr=True)
    print('Done!')


if __name__ == '__main__':
    theta_file = DEFAULT_MODEL
    target_seq = 'CTGAGTAGCTATGCGGCCAGCAGCGAGACGCTCAGCGTGAAGCGGCAGTATCCCTCTTTCCTGCGCACCATCCCCAATC'
    pam_idx = 42
    profile, rep_reads, in_frame = predictMutations(theta_file, target_seq, pam_idx)
    plotProfiles([profile], [rep_reads], [pam_idx], [False], ['Predicted'])

    import pdb;

    pdb.set_trace()
