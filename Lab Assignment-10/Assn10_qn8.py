n1 = int(input("Enter numerator\n"))
n2 = int(input("Enter denominator\n"))
try:
    print("RESULT = ",n1/n2)
except ZeroDivisionError as zde:
    print("Zero Divison Error Occured ....")
    print(zde)
finally:
    print("This is finally block it must be executed irrespective of exception.")