from Bio import SeqIO
import sys
import os
import numpy as np

def findSubThreshold(fastq):
    #pull out threshold from first line and remove that line so it doesnt interfere with interpretation from SeqIO
    with open(fastq, 'r') as file_in:
        data = file_in.read().splitlines(True)

    threshold = int(data[0])
    print(threshold)

    with open("temp_file.txt", 'w') as temp_out:
        temp_out.writelines(data[1:])

    records = list(SeqIO.parse("temp_file.txt", "fastq"))
    temp_in = open("temp_file.txt", "r")
    num_below = 0
    for rec in records:
        avg_qual = np.mean(rec.letter_annotations["phred_quality"])
        num_below = num_below+1 if avg_qual < threshold else num_below
    temp_in.close()
    os.remove('temp_file.txt')
    print(num_below)

if __name__ == "__main__":
    # set output file name using input file name as a template
    #dataset = sys.argv[1]
    dataset = 'datasets/ReadQualityDistribution_test.txt'
    outname = dataset.split("/")
    outname = "result_" + outname[-1]
    outfile = "results/" + outname

    findSubThreshold(dataset)
