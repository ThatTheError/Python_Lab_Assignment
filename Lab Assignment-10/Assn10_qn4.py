n1 = int(input("Enter Numerator\n"))
n2 = int(input("Enter denominator\n"))
try:
    print("RESULT = ",n1/n2)
except Exception as e:
    print(e)
else:
    print("No Exception is There\n")
finally:
    print("ThankYou\n")
