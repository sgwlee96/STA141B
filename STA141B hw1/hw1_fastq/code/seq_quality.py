from fastq_reader import *

import numpy as np

cleandata = '../data/dummy_cleaned2.fastq' # Path of the new dummy_cleaned2 data
seq_quality = [] #Sequence
cnt_seq = 3 #Sequence is in every fourth line 
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_seq:
        seq_quality.append(line.strip()) # delete /n
        cnt_seq += 4

# for idx, seq in enumerate(seq_quality):
#     print(seq[0])

name_quality = [] 
cnt_name = 0 # The name of the sequence starts at every first line
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_name:
        name_quality.append(line.strip()) #delete /n 
        cnt_name += 4
        

score = []

for seq in seq_quality:
    for i in seq:
        score.append(quality_score(i))
        

n = 160 # the length of the sequence 
npscore = np.array(score)
# calculates the average
avgResult = np.average(npscore.reshape(-1, n), axis=1)

max_value = max(avgResult) 
min_value = min(avgResult)


print("Highest quality seq: {}, quality: {}".format(name_quality[avgResult.argmax()],max_value)) 
print("Lowest quality seq: {}, quality: {}".format(name_quality[avgResult.argmin()],min_value))
