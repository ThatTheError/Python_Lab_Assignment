password = input("Enter a string : ")
upper,lower,digit=0,0,0
for i in password:
    if(i.isupper()):
        upper+=1
    elif(i.islower()):
        lower+=1
    elif(i.isdigit()):
        digit+=1
if(len(password)>7 and upper>0 and lower>0 and digit>0):
    print("Valid Password")
else:
    print("Invalid password")
