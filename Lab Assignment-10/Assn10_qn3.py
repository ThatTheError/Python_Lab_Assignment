ls = [12,0,"gopal",6]
try:
    print(ls)
    a = int(input("choose which value you want to assign for numerator\n"))
    b = int(input("choose which value you want to assign for denominator\n"))
    res = ls[a]/ls[b]
    print("RESULT = ",res)
except TypeError as te:
    print("type Error = ",te)
except ZeroDivisionError as zde:
    print(zde)
finally:
    print("Executed Sucessfully")