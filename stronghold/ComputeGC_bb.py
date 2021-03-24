handle = open("datasets/rosalind_gc.txt", 'r')
dna_dic = {}
val = []
while True:
    line = handle.readline()
    line = line.replace("\n","")
    if not line:
        if val:
            val = "".join(val)
            dna_dic.update({id: val})
        break

    if line.startswith(">"):
        if val:
            val = "".join(val)
            dna_dic.update({id: val})
        id = line.strip(">")
        val = []
    else:
        val.append(line)
handle.close()

gc_dic = {}
for id, val in dna_dic.items():
    gc_content = 100*(val.count("G") + val.count("C"))/len(val)
    gc_dic.update({id: gc_content})

max_id = max(gc_dic, key=gc_dic.get)
max_gc = max(gc_dic.values())
print(max_id)
print(round(max_gc,6))
