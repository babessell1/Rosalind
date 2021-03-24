import urllib.request
import sys
import re

# This is hacky and likely wont work well for datasets other than the practice but it wont let me download them so I can't test it
def extractBetween(text, left_marker, right_marker):
    try:
        out_str = re.search("".join([left_marker, "(.+?)", right_marker]), text).group(1)
    except AttributeError:
        out_str = ''

    return out_str

def findProteinFunction(protein_id):
    base_url = "https://www.uniprot.org/uniprot/"
    url = "".join([base_url, protein_id, ".txt"])
    content = urllib.request.urlopen(url)
    read_content = content.read().decode('utf-8')
    function_str = extractBetween(read_content, "3D-structure", "\nKW")
    function_str = function_str.strip(";")
    function_str = function_str.replace(" ", "")
    function = function_str.split(";")

    return function

if __name__ == "__main__":
    #protid = "Q5SLP9"
    protid = sys.argv[1]
    outfile = 'results/' + "result_ProteinDatabases.txt"

    with open(outfile, "w") as file:
        function = findProteinFunction(protid)
        for func in function:
            if func.startswith("DNA"):
                func = func[:3]+" "+func[3:]
                print(func)
                file.write(func+"\n")
