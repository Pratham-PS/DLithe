num = int(input())
print(num)
copy = num
rnum = 0
while num > 0:
    r = num / 10
    rnum = (rnum*10) + r
    num = num % 10
if copy == rnum:
    print("is a palindrome")
else:
    print("is not a palindrome")