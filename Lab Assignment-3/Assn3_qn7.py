n = int(input("Enter a no : "))
s = 0
while n>0:
    r = n%10
    s = s + r
    n = n // 10
print("SUM OF DIGIT'S = ",s)