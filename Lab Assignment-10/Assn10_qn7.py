n1 = int(input("Enter numerator\n"))
n2 = int(input("Enter denominator\n"))
try:
    print("RESULT = ",n1/n2)
except ZeroDivisionError as zde:
    print("Zero Divison Error Occured ....")
    print(zde)
else:
    print("This is else block this block will get executed when there is no exception in our code.")