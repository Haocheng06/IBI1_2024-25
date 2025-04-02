import re
outfile="C:\\IBI\\IBI_2024-25\\Practical7\\tata_genes.fa"
with open('C:\IBI\IBI_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r') as input_file, open(outfile,'w') as output_file:
    header=""
    sequence=""
    for line in input_file:
        line=line.strip()
        if line.startswith(">"):  # when meeting ">", it will start to process the last gene. So there is needed to add a part to process the gene in the ending of the input_file
            if re.search(r"TATA[AT]{1}A[AT]{1}", sequence):  
                output_file.write(header+"\n")
                for i in range(0, len(sequence), 60):
                    output_file.write(sequence[i:i + 60] + "\n")
            sequence=""  
            header=line[0:8]
        else:
            sequence+=line
    if re.search(r"TATA[AT]{1}A[AT]{1}", sequence):
        output_file.write(header + "\n")
        for i in range(0, len(sequence), 60):
            output_file.write(sequence[i:i + 60] + "\n")        
input_file.close()
output_file.close()
       


           