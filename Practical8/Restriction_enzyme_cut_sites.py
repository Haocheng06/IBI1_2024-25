def restriction_enzyme_cut(dna_sequence,enzyme_sequence):
    import re
    if re.search(r"[^ATCG]+",dna_sequence) or re.search(r"[^ATCG]+",enzyme_sequence):
        return("Your DNA sequence or Enzyme recognition ssequence is Wrong")
    cut_position=[]
    for i in range(len(dna_sequence)-len(enzyme_sequence)+1):
        current_sequence=dna_sequence[i:i+len(enzyme_sequence)]
        if current_sequence==enzyme_sequence:
            cut_position.append(str(i+1))
    if cut_position==[]:
        return(f"Error. There is no {enzyme_sequence}")
    else:
        return(f"enzyme cut position is at {cut_position}")
    
a=input("enter your DNA sequence!")    
b=input("please enter enzyme recognition sequence.")   
print(restriction_enzyme_cut(a,b))