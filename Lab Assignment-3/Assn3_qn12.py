n1 = int(input("Enter 1st no : "))
n2 = int(input("Enter 2nd no : "))
if n1>n2:
    it = n2
else:
    it = n1
for i in range(it,0,-1):
    if n1%i==0 and n2%i==0:
        break
print("Highest Common Factor = ",i)
