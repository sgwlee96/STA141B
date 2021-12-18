from fastq_reader import *

cleandata = '../data/dummy_cleaned2.fastq'

# Exercise 7.1

import re

cleandata = '../data/dummy_cleaned2.fastq'
seq2_quality = []
cnt_seq2 = 1
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_seq2:
        seq2_quality.append(line.strip())
        cnt_seq2 += 4

name_quality = []
cnt_name = 0
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_name:
        name_quality.append(line.strip())
        cnt_name += 4
                
        
# Count TCC
TCC_cnt = []

# Sort in descending order to make easier to pop the largest.
for idx, line in enumerate(seq2_quality):
    TCC_cnt.append(sorted(re.findall('((TCC)+)', line), reverse=True))

final_cnt = []

for i in range(25000):
    try: # It shows error when there's no TCC. 
        final_cnt.append(len(TCC_cnt[i][0][0]))
    except: # Thus, when the error occurs, append 0 to the empty list for count index number later.
        final_cnt.append(0)

maxTCCidx = final_cnt.index(max(final_cnt))



# Exercise 7.2

seq2_quality = []
cnt_seq2 = 1
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_seq2:
        seq2_quality.append(line.strip())
        cnt_seq2 += 4

name_quality = []
cnt_name = 0
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_name:
        name_quality.append(line.strip())
        cnt_name += 4
        

cnt_letters = []

for idx, line in enumerate(seq2_quality):
    cnt_letters.append(len(re.findall('(G.G)+', line)))

MAXG_G = cnt_letters.index(max(cnt_letters))
# print(name_quality[MAXG_G])


# Exercise 7.3

# A
A_cnt = []
        
for idx, line in enumerate(seq2_quality):
    A_cnt.append(sorted(re.findall('((A)+)', line), reverse=True))

A_final_cnt = []

for i in range(25000):
    try:
        A_final_cnt.append(len(A_cnt[i][0][0]))
    except:
        A_final_cnt.append(0)

A_maxTCCidx = A_final_cnt.index(max(A_final_cnt))


# T
T_cnt = []
        
for idx, line in enumerate(seq2_quality):
    T_cnt.append(sorted(re.findall('((T)+)', line), reverse=True))

T_final_cnt = []

for i in range(25000):
    try:
        T_final_cnt.append(len(T_cnt[i][0][0]))
    except:
        T_final_cnt.append(0)

T_maxTCCidx = T_final_cnt.index(max(T_final_cnt))

# G
G_cnt = []
        
for idx, line in enumerate(seq2_quality):
    G_cnt.append(sorted(re.findall('((G)+)', line), reverse=True))

G_final_cnt = []

for i in range(25000):
    try:
        G_final_cnt.append(len(G_cnt[i][0][0]))
    except:
        G_final_cnt.append(0)

G_maxTCCidx = G_final_cnt.index(max(G_final_cnt))


# C
C_cnt = []
        
for idx, line in enumerate(seq2_quality):
    C_cnt.append(sorted(re.findall('((C)+)', line), reverse=True))

C_final_cnt = []

for i in range(25000):
    try:
        C_final_cnt.append(len(C_cnt[i][0][0]))
    except:
        C_final_cnt.append(0)

C_maxTCCidx = C_final_cnt.index(max(C_final_cnt))


# N
N_cnt = []
        
for idx, line in enumerate(seq2_quality):
    N_cnt.append(sorted(re.findall('((N)+)', line), reverse=True))

N_final_cnt = []

for i in range(25000):
    try:
        N_final_cnt.append(len(N_cnt[i][0][0]))
    except:
        N_final_cnt.append(0)

N_maxTCCidx = N_final_cnt.index(max(N_final_cnt))

ATGCN_dic = {name_quality[A_maxTCCidx] : max(A_final_cnt), name_quality[T_maxTCCidx] : max(T_final_cnt),
            name_quality[G_maxTCCidx] : max(G_final_cnt), name_quality[C_maxTCCidx] : max(C_final_cnt),
            name_quality[N_maxTCCidx] : max(N_final_cnt)}

max_key = max(ATGCN_dic, key=ATGCN_dic.get)

print("Seq with longest TCC repeat: {}".format(name_quality[maxTCCidx]))
print("Seq with most matches to G_G: {}".format(name_quality[MAXG_G]))
print("Seq with longest of any one base: {}".format(max_key))

