from Bio import Entrez

def findGenBankRecords(dataset):
    with open(dataset) as file:
        lines = file.readlines()

    genus = lines[0].strip()
    start_date = lines[1].strip()
    end_date = lines[2].strip()

    search_term = genus + '[Organism] AND ("' + start_date + '"[PDAT]' + \
                                         ' : "' + end_date + '"[PDAT])'
    Entrez.email = 'babessell2@unl.edu'
    handle = Entrez.esearch(db="nucleotide", term=search_term)
    record = Entrez.read(handle)

    return record

if __name__ == "__main__":
    # set output file name using input file name as a template
    dataset = sys.argv[1]
    #dataset = 'datasets/rosalind_gbk.txt'
    outname = dataset.split("/")
    outname = "result_" + outname[-1]
    outfile = "results/" + outname

    # find shortest sequence, reformat to accepted format
    record = findGenBankRecords(dataset)
    with open(outfile, "w") as file:
        file.write(record["Count"])
    print(record["Count"])
