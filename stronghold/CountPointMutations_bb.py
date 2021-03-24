#!/usr/bin/python
import sys

def CalcHammingDistance(inFile):
    with open(inFile,'r') as handle:
        reads = handle.readlines()

    h_dist=0
    for i in range(len(min(reads))):
        if reads[0][i]!=reads[1][i] : h_dist+=1

    return str(h_dist)


if __name__ == "__main__":
    try:
        inFile = sys.argv[1]
        outFile = "results/result_" + inFile.split("/")[1]
    except:
        print("Incorrect arguments")

    try:
        h_dist = CalcHammingDistance(inFile)
        print(h_dist)

    except:
        print("Incorrect data format")

    with open(outFile,'w') as file:
        file.write(h_dist)
