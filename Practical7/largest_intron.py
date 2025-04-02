seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGAGGGCCTTA'
i=0
j=len(seq)-1
gt=[]
ag=[]
for i in range(len(seq)-1):
    if seq[i]=='G' and seq[i+1]=='T':
        gt.append(i)   
for j in range(len(seq)-1):
    if seq[j]=='A' and seq[j+1]=='G':
        ag.append(j)
     
max_seq=seq[int(gt[0]):int(ag[len(ag)-1])]
max_length=len(max_seq)
print(max_seq)
print(max_length)

    