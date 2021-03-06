import numpy as np

def findMotif(dna_str, mot_str):
    seq_len = len(dna_str)
    motif_idx = []
    for i in range(len(dna_str)):
        new_idx = dna_str.find(mot_str, i, seq_len)+1
        if new_idx>0 and new_idx not in motif_idx:
            motif_idx.append(new_idx)

    return motif_idx

seq = "CCACCGTAACACGTAACACACAGGTAACACGTAACACCGTAACACAGGTAACACGTGGTAACACTGTAACACTTCCGTGTAACACGTAACACGTAACACCGTAACACCATGTAACACTTCTTCCCATTGTAACACATGTCAACCGATGCGTAACACAGTTTCGTAACACAGTAACACTCTGTAACACGTAACACCGGTAACACGTAACACGTAACACTTCCGTAACACGAGTAACACTTCAGTAACACAGTAACACGCGTAACACCTGTAACACCAGTAACACTGTAACACGTAACACGTAACACTTCTTGGTCTTACGTAACACGTAACACCTGTGGTAACACCGTAACACGTAACACGTAACACGTAACACGTAACACATTAGGCTGTCTGTAACACGTAACACGTAACACCTATCGGGTAACACTGTAACACTAGTAACACCGTAACACTATGCGCAGTAACACTTGTAACACGTAACACCTCCGGGTAACACGTAACACGTAACACGTAACACGGGTAACACGGTGTGTAACACGTAACACGTAACACGTAACACGTAACACAACGTAACACTTTAGCATGTAACACGTAACACGTAACACCTCGCGTAACACCCCTAGTAACACCGTCGTTCGTAACACGTAACACTGTGTAACACTGGTTGCAGGTAACACCGTAACACCAAGGTAACACCGCGTAACACTGTAACACGGTAACACGGTAACACGTAACACAGTAACACAGGTAACACGTAACACGTAACACGCGTAACACAAGAAGGTAACACGTAACACCCGTAACACGGTAACACGGTAACACTGTAACACGTAACACGTAACACGTAACGTAACACGTAACACATTAGTAACACGTAACACTTGGGTAACACGTAACACTGTAACACGCGTAACACGTAACACCGTAACAC"
sub = "GTAACACGT"

result = findMotif(seq, sub)
result_str = "".join([idx for idx in str(result)])
result_str = result_str.replace(",","")
result_str = result_str.replace("[","")
result_str = result_str.replace("]","")
print(result_str)
