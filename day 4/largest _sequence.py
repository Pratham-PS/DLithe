lists = [1,2,-2,5,4,-4,6,3,-3,-6]
max = 0
final = []
for i in range(0,len(lists)):
    sum = 0
    count = 0
    flag = 0
    new = []
    for j in range(i,len(lists)): 
        sum = sum+int(lists[j])
        count +=1
        if sum == 0 and flag == 0:
            flag = 1
        new.append(lists[j])
    if flag == 1 and sum==0:
        if count > max:
            max = count
            final = new
print(final)
