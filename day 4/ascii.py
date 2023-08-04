print("enter the string")
s = "pransh"
print(s)
string = list(s)
print("enter the shift")
shift = [4,5,6,1,2,2]
print(shift)
sums = sum(shift)
alp = "abcdefghijklmnopqrstuvwxyz"
d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
a = shift[1]+d[string[1]]
for i in range(0,len(string)):
    index = d[string[i]]
    index = index + sums
    string[i]=alp[index%26]
    sums = sums - shift[i]
output = "".join(string)
print(output)