from fastq_reader import *

cleandata = '../data/dummy_cleaned2.fastq'

base_quality = [] # Shows the Base of each sequence
cnt_base = 1
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_base:
        base_quality.append(line.strip())
        cnt_base += 4
        
# print(base_quality)

seq_quality = []
cnt_seq = 3
for idx,line in enumerate(open(cleandata).readlines()):
    if idx == cnt_seq:
        seq_quality.append(line.strip())
        cnt_seq += 4
        
# print(seq_quality)

base_quality = ''.join(base_quality)
seq_qaulity = ''.join(seq_quality)

A_idx = []
T_idx = []
G_idx = []
C_idx = []
N_idx = []


for i in  range(len(base_quality)):
    if base_quality[i] == "A":
      A_idx.append(i)
    
    if base_quality[i] == "T":
      T_idx.append(i)
    
    if base_quality[i] == "G":
      G_idx.append(i)
    
    if base_quality[i] == "C":
      C_idx.append(i)
    
    if base_quality[i] == "N":
      N_idx.append(i)
    
    
# print(A_idx[:30])
# print(T_idx[:30])
# print(G_idx[:30])
# print(C_idx[:30])
# print(N_idx[:30])

A_qual = []
T_qual = []
G_qual = []
C_qual = []
N_qual = []

joined_seq_quality = ''.join(seq_quality)

# For base A
for i in A_idx:
    A_qual.append(joined_seq_quality[i])

A_score_lst = []

for i in A_qual:
    A_score_lst.append(quality_score(i))
    

# For base T
for i in T_idx:
    T_qual.append(joined_seq_quality[i])

T_score_lst = []

for i in T_qual:
    T_score_lst.append(quality_score(i))
    


# For base G
for i in G_idx:
    G_qual.append(joined_seq_quality[i])

G_score_lst = []

for i in G_qual:
    G_score_lst.append(quality_score(i))
    

# For base C
for i in C_idx:
    C_qual.append(joined_seq_quality[i])

C_score_lst = []

for i in C_qual:
    C_score_lst.append(quality_score(i))
    

# For base N
for i in N_idx:
    N_qual.append(joined_seq_quality[i])

N_score_lst = []

for i in N_qual:
    N_score_lst.append(quality_score(i))
    
# print the result
print(f"base: A, quality: {np.mean(A_score_lst)}")   
print(f"base: T, quality: {np.mean(T_score_lst)}")  
print(f"base: G, quality: {np.mean(G_score_lst)}")    
print(f"base: C, quality: {np.mean(C_score_lst)}")
print(f"base: N, quality: {np.mean(N_score_lst)}")

