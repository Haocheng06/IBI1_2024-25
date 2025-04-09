def restriction_enzyme_cut(dna_sequence,enzyme_sequence):
    
    cut_position=[]
    for i in range(len(dna_sequence)-4):
        current_sequence=dna_sequence[i:i+4]
        if current_sequence==enzyme_sequence:
            cut_position.append(str(i+1))
    if cut_position==[]:
        return("Error. There is no ACGT")
    else:
        return(f"enzyme cut position is at {cut_position}")
    
a=input("enter your DNA sequence!")    
b=input("please enter enzyme recognition sequence.")   
print(restriction_enzyme_cut(a,b))