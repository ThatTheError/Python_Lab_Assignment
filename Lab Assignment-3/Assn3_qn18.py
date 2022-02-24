n = int(input("Enter n : "))
s = 1
for i in range(2,n+1):
    if i%2==0:
        s = s-1/i
    else:
        s = s+1/i
print("RESULT = ",s)
