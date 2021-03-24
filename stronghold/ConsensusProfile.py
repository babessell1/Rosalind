#!/usr/bin/env python

import sys
import numpy as np

def findConsensusString(dna_matrix):
    a_str = "A:"
    c_str = "C:"
    g_str = "G:"
    t_str = "T:"
    consensus_str = ""

    for i in range(len(dna_matrix[0,:])):
        a_sum = sum(dna_matrix[:,i]=="A")
        c_sum = sum(dna_matrix[:,i]=="C")
        g_sum = sum(dna_matrix[:,i]=="G")
        t_sum = sum(dna_matrix[:,i]=="T")

        vals, cnts = np.unique(dna_matrix[:,i], return_counts=True)
        idx = np.argmax(cnts)
        consensus_str += vals[idx]

        a_str += " " + str(a_sum)
        c_str += " " + str(c_sum)
        g_str += " " + str(g_sum)
        t_str += " " + str(t_sum)
        profile_str = a_str + "\n" + c_str + "\n" + g_str + "\n" + t_str

    return consensus_str, profile_str

def readFASTA(fastaFile):
    with open(fastaFile,'r') as handle:
        lines = handle.readlines()
        dna_matrix = []

    cnt=0
    new_string = ""
    print(len(lines))
    for line in lines:
        if line.startswith(">") and cnt!=0:
            if len(dna_matrix)<1 : dna_matrix = np.array(list(new_string))
            else : dna_matrix = np.vstack((dna_matrix,list(new_string)))
            new_string = ""

        elif cnt!=0:
            new_string += line.strip("\n")
        cnt+=1
    dna_matrix = np.vstack((dna_matrix,list(new_string)))
    print(dna_matrix)
    return dna_matrix

if __name__ == "__main__":
    try:
        dataFile = sys.argv[1]
        outFile = "results/result_" + dataFile.split("/")[1]
    except:
        print("Takes 1 argument, a FASTA formated list of no more than 10 DNA\
               strings less than 1 kbp long")

    dna_matrix = readFASTA(dataFile)
    consensus_str, profile_str = findConsensusString(dna_matrix)

    print(consensus_str)
    print(profile_str)
    with open(outFile,'w') as file:
        file.write(consensus_str+'\n'+profile_str)
