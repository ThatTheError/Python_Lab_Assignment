n = int(input("Enter a no : "))
no,num = n,n
arm,c = 0,0
while n>0:
    r = n%10
    c = c+1
    n = n//10
while no>0:
    r = no%10
    arm = arm + r**c
    no = no//10
if arm==num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")