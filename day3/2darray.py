a = [[1,2,0],[4,2,3],[0,3,2]]
c_i=[]
c_j=[]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i][j]==0:
            c_i.append(i)
            c_j.append(j)
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i in c_i or j in c_j:
            a[i][j] = 0
print(a)
