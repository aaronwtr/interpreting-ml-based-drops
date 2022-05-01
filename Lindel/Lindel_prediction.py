#!/usr/bin/env python 
# Author: Will Chen
"""
1. All functions are tested under python3.5 and python 3.6
2. Add Lindel folder to your python path.
3. y_hat is the prediction of all ~450 classes of indels <30bp.
4. fs is the frameshift ratio for this sequence.
5. Input should be 65bp (30 bp upstream and 35 bp downstream of the cleavage site)
usage: pyton Lindel_predction.py your_sequence_here your_file_name_here(can be gene name or guide name you designed)
"""

import pickle as pkl
from tqdm import tqdm
import pandas as pd

import Lindel
import config
import os
from Lindel.Predictor import *
from get_shap_values import check_pam


def predict_all_samples(save=False):
    for i in tqdm(range(guideset.shape[0])):
        cont = False
        current_sample = guideset.iloc[i]['ID']
        sample_idx = int(current_sample[5:])
        for index, row in guideset.iterrows():
            if sample_idx == index:
                pam_idx = row['PAM Index']
                nt_to_delete = pam_idx - 33  # We need to make sure the PAM is at the 33 idx
                seq = row['TargetSequence'][nt_to_delete:]
                if check_pam(seq):
                    break
                else:
                    cont = True
        if cont:
            continue

        filename = current_sample.split('_')[0:2]
        filename = '_'.join(filename)
        y_hat, fs = gen_prediction(seq, weights, prerequesites)
        filename += '_fs=' + str(round(fs, 3)) + '.txt'
        rev_index = prerequesites[1]
        pred_freq = {}
        for j in range(len(y_hat)):
            if y_hat[j] != 0:
                pred_freq[rev_index[j]] = y_hat[j]
        pred_sorted = sorted(pred_freq.items(), key=lambda kv: kv[1], reverse=True)
        write_file(seq, pred_sorted, pred_freq, filename)

        path_to_file = f'repair_outcomes/cache/{filename}'
        current_repair_outcome = open_file(path_to_file)
        column_names = ['Target sequence outcome', 'Integration frequency', 'Indel label']
        current_repair_outcome.columns = column_names
        indel_name = current_repair_outcome.iloc[0]['Indel label']
        indel_name = indel_name.split('+')[0]
        indel_name = indel_name.split(' ')[0]
        indel_length = int(indel_name[1:])

        if save:
            if indel_name[0] == 'D' and indel_length >= 15:
                np.savetxt(f'repair_outcomes/candidate_repair_outcomes/deletions/{current_sample}_{indel_name}.txt',
                           current_repair_outcome.values, fmt='%s', delimiter='\t')
            else:
                np.savetxt(f'repair_outcomes/low_freq_repair_outcomes/{current_sample}_{indel_name}',
                           current_repair_outcome.values, fmt='%s', delimiter='\t')

    return


def predict_single_sample(current_oligo, guideset, save=False):
    w = pkl.load(open(os.path.join(Lindel.__path__[0], "Model_weights.pkl"), 'rb'))
    pres = pkl.load(open(os.path.join(Lindel.__path__[0], 'model_prereq.pkl'), 'rb'))
    for index, row in guideset.iterrows():
        if int(current_oligo) == index:
            pam_idx = row['PAM Index']
            nt_to_delete = pam_idx - 33  # We need to make sure the PAM is at the 33 idx
            seq = row['TargetSequence'][nt_to_delete:]
            if check_pam(seq):
                break
            else:
                return 0

    filename = f'Oligo{current_oligo}'

    y_hat, fs = gen_prediction(seq, w, pres)
    filename += '_fs=' + str(round(fs, 3)) + '.txt'
    rev_index = pres[1]
    pred_freq = {}
    for i in range(len(y_hat)):
        if y_hat[i] != 0:
            pred_freq[rev_index[i]] = y_hat[i]
    pred_sorted = sorted(pred_freq.items(), key=lambda kv: kv[1], reverse=True)

    write_file(seq, pred_sorted, pred_freq, filename)
    path_to_file = f'repair_outcomes/cache/{filename}'
    current_repair_outcome = open_file(path_to_file)

    column_names = ['Target sequence outcome', 'Integration frequency', 'Indel label']
    current_repair_outcome.columns = column_names
    indel_names = list(current_repair_outcome['Indel label'])
    int_freqs = list(current_repair_outcome['Integration frequency'])

    indel_names = [x.split('+')[0] for x in indel_names]
    indel_names = [x.split('  ')[0] for x in indel_names]

    indels_done = []
    for indel in indel_names:
        count = 0
        if indel not in indels_done:
            count += 1
            for i in range(len(indel_names)):
                if indel_names[i] == indel:
                    indel_names[i] = indel + '_' + str(count)
                    indel_names[i] = indel_names[i].split('_')[0] + '_' + indel_names[i].split('_')[1]
                    count += 1
        indels_done.append(indel)

    pred_freq = {}
    for i in range(len(int_freqs)):
        if int_freqs[i] != 0:
            pred_freq[indel_names[i]] = int_freqs[i]/100
    pred_sorted = sorted(pred_freq.items(), key=lambda kv: kv[1], reverse=True)
    # transform pred_sorted into a dictionary
    pred_sorted = {k: v for k, v in pred_sorted}

    return pred_sorted


if __name__ == '__main__':
    weights = pkl.load(open(os.path.join(Lindel.__path__[0], "Model_weights.pkl"), 'rb'))
    prerequesites = pkl.load(open(os.path.join(Lindel.__path__[0], 'model_prereq.pkl'), 'rb'))
    guideset = pd.read_csv(f"{config.path}/guideset_data.txt", sep='\t')

    predict_all_samples()