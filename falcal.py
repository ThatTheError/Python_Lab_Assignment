#               FAULTY CALCULATOR
print("enter what operation you want to do:")
print("""enter 1 for addition
enter 2 for substraction
enter 3 for multiplication
and 4 for division""")
no=int(input())
if(no>4):
    exit("cant perform the operation")
print("enter 1st value")
val1=int(input())
print("enter 2nd value")
val2=int(input())
if no==1:
    if val1==11 and val2==21:
        print("0")
    else:
        print("the answer is",val1+val2)
elif no==2:
    if val1==22 and val2==31:
        print("0")
    else:
        print("the substract valuse is",val1-val2)
elif no==3:
    if val1==33 and val2==41:
        print("0")
    else:
        print("the multiplied value is",val1*val2)
elif no==4:
    if val1==44 and val2==51:
        print("0")
    else:
        print("the divided value is",float(val1)/float(val2))


