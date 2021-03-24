import sys
from Bio import Entrez, SeqIO
import re

def findShortestSequence(dataset):
    with open(dataset) as file:
        entry_ids = file.readline().strip().split(" ")

    Entrez.email = "babessell2@unl.edu"
    handle = Entrez.efetch(db="nucleotide", id=entry_ids, rettype="fasta")
    short_fasta = min(list(SeqIO.parse(handle,"fasta")), key=len).format("fasta")

    return short_fasta

def fastaReformat(fasta): # to satisfy Rosalinds 70 nucleotides/line format
    spl = fasta.split("\n")
    seq = "".join(spl[1:])
    seq = re.sub("(.{70})", "\\1\n", seq, 0, re.DOTALL) #add newline every 70 characters

    return spl[0] + "\n" + seq


if __name__ == "__main__":
    # set output file name using input file name as a template
    dataset = sys.argv[1]
    dataset = 'datasets/DataFormats_test.txt'
    outname = dataset.split("/")
    outname = "result_" + outname[-1]
    outfile = "results/" + outname

    # find shortest sequence, reformat to accepted format
    short_fasta = findShortestSequence(dataset)
    short_fasta = fastaReformat(short_fasta)
    with open(outfile, "w") as file:
        file.write(short_fasta)
    print(short_fasta)
