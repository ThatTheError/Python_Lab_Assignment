n = int(input("Enter a no : "))
def prime(num):
    c=0
    for i in range(2,num):
        if num%i==0:
            c+=1
    return c
x=prime(n)
if x==0:
    print("Prime")
else:
    print("Not a prime")