n = int(input())
max = 0
grt = 0
for i in range(0,n):
    new = int(input())
    if new > max:
        max = new
        grt += 1
print(grt)