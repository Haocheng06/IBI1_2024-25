import re
name=input("input GTAG, GCAG, or ATAC :")
outfile=f"C:\\IBI\\IBI_2024-25\\Practical7\\{name}_spliced_genes.fa"
con_header=[]
con_sequence=[]
with open('C:\\IBI\\IBI_2024-25\\Practical7\\tata_genes.fa','r') as input_file, open(outfile,'w') as output_file:
    sequence=""
    for line in input_file:
        line=line.strip()
        if line.startswith(">"):  
            if re.search(name, sequence):  
                con_header.append(header)
                con_sequence.append(sequence)
            sequence=""  
            header=line[1:8]
        else:
            sequence+=line
    if re.search(name, sequence):
        con_header.append(header)
        con_sequence.append(sequence)         
    for i in range(len(con_sequence)):
        count=0
        for j in range(0,len(con_sequence[i])-6,1):
            if re.search(r'TATA[AT]{1}A[AT]{1}',con_sequence[i][j:j+7]):
                count+=1
        output_file.write(con_header[i]+"\t"+str(count)+"\n"+con_sequence[i]+"\n")
input_file.close()
output_file.close()