string = input("Enter a string")
upper,lower,space,digit=0,0,0,0
for i in string:
    if(i.isupper()):
        upper+=1
    elif(i.islower()):
        lower+=1
    elif(i.isspace()):
        space+=1
    elif(i.isdigit()):
        digit+=1
print("UPPER = {0} LOWER = {1} SPACE = {2} DIGITS = {3}".format(upper,lower,space,digit))

