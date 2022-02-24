"""
Define a class Height, with attributes feet and inch. Write the program to enter the
height of two persons and find the difference between them.
"""

class Height:
    def __init__(self,feet,inch):
        self.feet = feet
        self.inch = inch
    def __sub__(self, other):
        inchdiff = abs((self.feet*12+self.inch)-(other.feet*12+other.inch))
        return(inchdiff//12," FEET ",inchdiff-(inchdiff//12*12)," INCH")
if __name__=="__main__":
    print("INPUT-1")
    feet = int(input("Enter the feet"))
    inch = int(input("Enter the inch"))
    ob1 = Height(feet,inch)
    print("INPUT-2")
    feet = int(input("Enter the feet"))
    inch = int(input("Enter the inch"))
    ob2 = Height(feet, inch)
    print("HEIGHT DIFFERENCE = ",ob1-ob2)