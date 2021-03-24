#!/usr/bin/python
import sys
from re import findall

def makeCodonDictionary(codon_table):
    codon_dict = {}
    with open(codon_table, 'r') as handle:
        entries = "".join(handle.readlines()).split()

    idx_rna = 0
    idx_aa = 1
    for i in range(int(len(entries)/2)):
        new_rna = entries[idx_rna]
        new_aa = entries[idx_aa]
        codon_dict[new_rna] = new_aa
        idx_rna+=2
        idx_aa+=2

    return codon_dict


def RNA2AA(rna_str, codon_dict):
    codons = findall('.{1,3}', rna_str)
    aa_list = len(codons)*[""]
    for i in range(len(codons)):
        aa_list[i] = codon_dict[codons[i]]

    aa_str = "".join(aa_list).strip("Stop")
    aa_str_sep = aa_str.split("Stop")
    aa_str_list = len(aa_str_sep)*[""]
    for i in range(len(aa_str_sep)) : aa_str_list[i] = aa_str_sep[i].strip("Stop")

    return aa_str_list


if __name__ == "__main__":
    try:
        dataFile = sys.argv[1]
        tableFile = sys.argv[2]
        outFile = "results/result_" + dataFile.split("/")[1]
    except:
        print("Improper Arguments, first should be a file with single string of \
          RNA information, second should be a tab seperated codon table")

    with open(dataFile,'r') as handle:
        rna_str = "".join(handle.readlines())

    codon_dict = makeCodonDictionary(tableFile)
    aa_str_list = RNA2AA(rna_str, codon_dict)
    file = open(outFile, 'w')
    for i in range(len(aa_str_list)):
        file.write(2*"\n"+aa_str_list[i]) if i>0 else file.write(aa_str_list[i])
        print(aa_str_list[i]+"\n")
