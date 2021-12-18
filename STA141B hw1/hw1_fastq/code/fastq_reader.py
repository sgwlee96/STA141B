import re
from collections import Counter

def quality_score(quality_chr):
    # change numeric to string
    if quality_chr in [0,1,2,3,4,5,6,7,8,9]:
        quality_chr = str(quality_chr)
    
    # Here we can find that a = 33, b = 40
    ans = (ord(quality_chr) - 33)/40
    
    return float(ans) # replace this with the float score

# Function that return ngram with frequency
def ngram_freq(sequence, n=1):
    
    # Use zip
    ngrams = zip(*[sequence[i:] for i in range(n)] )
    counts = Counter(ngrams)

    # turn Counts to dict.type
    token_dic = dict(counts.most_common())
    total = sum(token_dic.values())

    key_lst = [''.join(tups) for tups in token_dic.keys()]
    val_lst = list(token_dic.values())

    final_dic = dict(zip(key_lst, val_lst))

    for k, v in final_dic.items():
        final_dic[k] = v/total
        
    return final_dic # replace with the dictionary described


#Function that shows similarity of two sequence by ngram
def ngram_sim(seq1, se2, n=1):
    set1 = set(ngf1)
    set2 = set(ngf2)

    sumlst = []

    for base in set1.intersection(set2):
    #     print(base, ngf1[base], ngf2[base])
        sumlst.append((ngf1[base]*ngf2[base])**0.5)
        
    return sum(sumlst) # replace with the float score