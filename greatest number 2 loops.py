n = int(input())
arr = []
for i in range(0,n):
    arr.append(input())
print(arr)
grt = 1
a = 0
max = arr[0]
for i in range(1,n):
    if arr[i] > max:
        max = arr[i]
        grt += 1
print(grt)