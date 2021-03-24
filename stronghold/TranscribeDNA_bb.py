
def dna2rna(dna_str):
    return dna_str.replace("T", "U")

with open("datasets/rosalind_rna.txt") as handle:
    dna_str = handle.read()

dna_str = dna_str.replace("\n", "")

rna_str = dna2rna(dna_str)
print(rna_str)
