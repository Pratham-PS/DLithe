a = [1,3,5,2,4]
res = [] 
sum = 6
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == sum:
            res.append((a[i],a[j]))
for i in res:
    print(i)

