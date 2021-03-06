import io, os, csv, sys, re
import numpy as np
import pylab as PL
import Bio.Seq
from selftarget.util import getPlotDir
from selftarget.indel import tokFullIndel
from selftarget.profile import readSummaryToProfile, fetchRepresentativeCleanReads, getProfileCounts
from selftarget.oligo import getFileForOligoIdx
from selftarget.plot import saveFig

def padReadForIndel(read_seq, indel, pam_idx):
    itype,isize,details,muts = tokFullIndel(indel)
    red_idxs, green_idxs = set(), set()
    if itype == 'D':
        read_seq = read_seq[:pam_idx-3+details['L']+details['C']+1] + ' '*isize + read_seq[pam_idx-3+details['L']+details['C']+1:]
        green_idxs = set(range(pam_idx-3+details['L']+1, pam_idx-3+details['L']+1+details['C']))
    if itype == 'I':
        green_idxs = set(range(pam_idx-3+details['L']+1, pam_idx-3+details['L']+1+details['C']))
        red_idxs = set(range(pam_idx-3+details['L']+1+details['C'],pam_idx-3+details['L']+details['C']+1+isize))
    return read_seq, red_idxs, green_idxs
    
def plotSeqLetterwise(seq, y, pam_idx, red_idxs=set(), green_idxs=set(), default_clr='black'):
    for i,nt in enumerate(seq):
        if i in red_idxs:	clr = 'red'
        elif i in green_idxs:	clr = 'green'
        else:	clr = default_clr
        xloc = i-pam_idx+3
        if xloc > 0:	xloc += 0.1
        if xloc > -35 and xloc <= 35:
            PL.text(xloc,y, nt, verticalalignment='bottom', horizontalalignment='left', color=clr)


def getAvgPreds(profiles, oligo):
    ocounts = [getProfileCounts(p1) for p1 in profiles]
    counts = [{indel: (cnt, indel, perc1a, perc1b) for (cnt, indel, perc1a, perc1b) in x if indel != '-'} for x in ocounts]

    num_top = len(counts[0])
    top_indels = [[y[1] for y in x[:num_top]] for x in ocounts]
    union_top_indels = set()
    for x in top_indels: union_top_indels = union_top_indels.union(set(x))

    for indel in union_top_indels:
        for count in counts:
            if indel not in count:
                count[indel] = (0, indel, 0.0, 0.0)
    union_top_indels = [x for x in union_top_indels]

    top_av_percs = [(np.mean([x[indel][-1] for x in counts]), 'Oligo_' + str(oligo) + '_' + str(indel)) for indel in union_top_indels]
    top_av_percs.sort(reverse=True)

    # top_av_percs = [x for x in top_av_percs if x[1].split('_')[2] == 'I2' and x[0] > 0.3]

    return top_av_percs

    
def plotProfiles(profiles, rep_reads, pam_idxs, reverses, labels, oligo, title='', max_lines=60):
    if len(profiles) == 0: raise Exception('Empty list of profiles')
    
    colors = ['C0', 'C2', 'C1']

    PL.rcParams['svg.fonttype'] = 'none'
    ocounts = [getProfileCounts(p1) for p1 in profiles]
    counts = [{indel: (cnt,indel,perc1a,perc1b) for (cnt,indel,perc1a,perc1b) in x} for x in ocounts]
    nonnull_reads = [len(counts[0]) - 1]

    labels = ['%s (%d Reads)' % (tit,nn) for (tit,nn) in zip(labels, nonnull_reads)]

    #Fetch the indels to display as union of top N indels across profiles
    num_top = 20
    top_indels = [[y[1] for y in x[:num_top]] for x in ocounts]
    union_top_indels = set()
    for x in top_indels: union_top_indels = union_top_indels.union(set(x))
    
    for indel in union_top_indels:
        for count in counts:
            if indel not in count:
                count[indel] = (0,indel,0.0,0.0)
    union_top_indels = [x for x in union_top_indels]
    indel_toks = [tokFullIndel(indel) for indel in union_top_indels]
    max_insert = max([0] + [toks[1] for toks in indel_toks if toks[0] == 'I'])

    top_av_percs = getAvgPreds(profiles, oligo)
    if len(top_av_percs) == 0:
        return 0

    max_indels = 6  #max_lines/len(profiles)

    #Figure out Trims
    null_reads = [x['-'] if '-' in x else [x[y[1]] for y in ocnt if y[1] in x][0] for x,ocnt in zip(rep_reads, ocounts)]
    null_reads = [Bio.Seq.reverse_complement(x) if rev else x for x,rev in zip(null_reads, reverses)]
    pam_idxs = [len(x) - pam if rev else pam for x,pam,rev in zip(null_reads, pam_idxs, reverses)]
    min_null, pam_idx = min([(len(null),pidx) for (null, pidx) in zip(null_reads, pam_idxs)])
    Ls = [x - pam_idx for x in pam_idxs]
    Rs = [L + min_null - len(null) for (L,null) in zip(Ls, null_reads)]

    #Plot
    scale_factor = 30.0/max([x[1][3] for x in ocounts])
    fig = PL.figure(figsize=(15, 10))
    fig.patch.set_visible(False)
    ax = PL.gca()
    ax.axis('off')
    N = min(len(union_top_indels), max_indels)
    line_height = 0.8
    PL.ylim( (0,(N+1.0)*line_height) )
    bar_ypos, bar_len = [[] for x in profiles], [[] for x in profiles]
    for i, (av_perc, indel) in enumerate(top_av_percs):
        indel = indel.split('_')[2:]
        indel = '_'.join(indel)
        if i > max_indels: break
        for repr, cnts, rev, L1, R1, j in zip(rep_reads, counts, reverses, Ls, Rs, range(len(Rs))):
            (cnt1,indel1,perc1a,perc1b) = cnts[indel]
            if indel in repr:
                if R1 == 0: R1 = len(repr[indel])
                seq = Bio.Seq.reverse_complement(repr[indel])[L1:R1] if rev else repr[indel][L1:R1]
                padded_seq, red_idxs, green_idxs = padReadForIndel(seq, indel, pam_idx)
                plotSeqLetterwise(padded_seq, (N-i+j*1.0/len(profiles))*line_height, pam_idx, red_idxs=red_idxs, green_idxs=green_idxs)
            if indel != '-':
                bar_ypos[j].append((N-i+(j+0.5)*1.0/len(profiles))*line_height)
                bar_len[j].append(perc1b*scale_factor)
    hist_loc = 45
    for bar1_ypos, bar1_len, label1,clr in zip(bar_ypos, bar_len, labels,colors):
        PL.barh(bar1_ypos, bar1_len, height=0.8*line_height/len(profiles), left=hist_loc, label=label1, color=clr )
        for (ypos, blen) in zip(bar1_ypos, bar1_len):
            PL.text(hist_loc+blen+1,ypos-0.1/len(profiles)*line_height, '%.1f%%' % (blen/scale_factor))
    xlims = (-45,hist_loc + max([max(x) for x in bar_len]) + 5)
    PL.xlim( xlims )

    for i, (av_perc, indel) in enumerate(top_av_percs):
        if i > max_indels: break
        PL.text(xlims[0]-5,(N-i+0.5)*line_height,'_'.join(indel.split('_')[2:]), fontweight='bold')
        PL.plot(xlims,[(N-i)*line_height, (N-i)*line_height],'lightgrey')
    PL.plot([0,0],[0,N*line_height],'k--')
    PL.plot([hist_loc,hist_loc],[0,N*line_height],'k')
    PL.xticks([])
    PL.yticks([])
    PL.legend(loc='upper right')
    PL.title(title)
    PL.subplots_adjust(left=0.05,right=0.95,top=0.95, bottom=0.05)
