
def countNucFrequency(seq):
    freq_dict = {"A": 0, "C":0, "G": 0, "T": 0}
    for nuc in seq:
        freq_dict[nuc] += 1
    return freq_dict

with open("datasets/rosalind_ini.txt") as handle:
    dna_str = handle.read()

dna_str = dna_str.replace("\n", "")
print(dna_str)
result = countNucFrequency(dna_str)

print(' '.join([str(val) for key, val in result.items()]))
