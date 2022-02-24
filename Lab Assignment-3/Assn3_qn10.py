n = input("Enter a binary no : ")
ls = list(n)
c,dec = 0,0
for i in ls[::-1]:
    dec = dec+int(i)*2**c
    c+=1
print("Decimal Equivalent = ",dec)
