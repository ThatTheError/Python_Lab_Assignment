n = int(input("Enter a decimal no : "))
binlist = []
while n>2:
    r = n%2
    binlist.append(r)
    n = n//2
binlist.append(n)
binlist = binlist[::-1]
for i in binlist:
    print(i,end='')
