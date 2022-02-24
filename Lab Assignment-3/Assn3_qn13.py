ls = []
x = 1
while(x):
    n = int(input("Enter a no : "))
    ls.append(n)
    x = int(input("Enter 1 for continue 0 for exit"))
print(ls)
negative,zero,positive=0,0,0
for i in ls:
    if i==0:
        zero+=1
    elif i<0:
        negative += 1
    else:
        positive+=1
print("positive no = ",positive," Negative no = ",negative," Zeros = ",zero)

