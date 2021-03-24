from Bio import SeqIO
import sys

def convertFASTQ(fastq):
    records = list(SeqIO.parse(fastq, "fastq"))
    file = open(outfile, "w")
    for rec in records:
        print(rec.format("fasta"))
        file.write(rec.format("fasta"))
    file.close()

if __name__ == "__main__":
    # set output file name using input file name as a template
    dataset = sys.argv[1]
    #dataset = 'datasets/fastq2fasta_test.txt'
    outname = dataset.split("/")
    outname = "result_" + outname[-1]
    outfile = "results/" + outname

    convertFASTQ(dataset)
    
