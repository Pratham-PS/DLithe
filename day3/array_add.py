a = [1,2,3,3,5,6,6]
b = [6,3,4,5]
c = []
i = len(a) - 1 
j = len(b) - 1
sum = 0
carry = 0
while i > -1 or j > -1 or carry > 0:
    sum = (a[i] if i > -1 else 0) + (b[j] if j > -1 else 0) + carry
    carry = sum // 10
    c.insert(0,sum%10)
    i -= 1
    j -= 1
print(c)
