def range_check(n):
    if n<1 or n>30:
        raise ValueError
try:
    n = int(input("Enter a Number with in the range of 1-30\n"))
    range_check(n)
except ValueError:
    print("Entered value is not in the given range")
else:
    print("Entered value is within the range")
