def fact(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac
s = 0
for i in range(1,5):
    s = s+(i/fact(i))
print("Result = ",s)
