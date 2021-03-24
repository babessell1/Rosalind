def complementDNA(dna_str):
    rev_char = list(dna_str[::-1])
    pos = 0
    for nuc in rev_char:
        if nuc == "A":
            rev_char[pos] = "T"
        elif nuc == "T":
            rev_char[pos] = "A"
        elif nuc == "C":
            rev_char[pos] = "G"
        elif nuc == "G":
            rev_char[pos] = "C"
        else:
            error("INVALID SEQUENCE")
        pos+=1

    rev_str = "".join([nuc for nuc in rev_char])
    return rev_str

#dna_seq = "AAAACCCGGT"
with open("datasets/rosalind_revc.txt") as handle:
    dna_str = handle.read()

dna_seq = dna_str.replace("\n", "")
comp_seq = complementDNA(dna_seq)
print(comp_seq)
