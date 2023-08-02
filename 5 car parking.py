i = int(input())
j = int(input())
line = 0
max = 0
for a in range(j):
    sum = 0
    for b in range(i):
        sum += int(input())
    if sum > max:
        line = a+1
        max = sum
print(line)
