def prime(num):
    c=0
    for i in range(2,num):
        if num%i==0:
            c+=1
    return c
n = int(input("Enter n : "))
for i in range(1,n+1):
    x=prime(i)
    if x==0:
        print(i)

