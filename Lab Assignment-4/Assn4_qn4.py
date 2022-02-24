pas = input("Enter password : ")
c=0
pas = list(pas)
for i in pas:
    if ord(i)>=32 and ord(i)<=47 or ord(i)>=58 and ord(i)<=64 or ord(i)>=91 and ord(i)<=96 and ord(i)>=123 or ord(i)<=126:
        c=c+1
if len(pas)>=8 and c>0:
    print("valid password")
else:
    print("Invalid Password")

