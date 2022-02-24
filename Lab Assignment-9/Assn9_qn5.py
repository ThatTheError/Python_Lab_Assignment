"""
Define the class Point, with the attributes such as x & y-coordinate and define a method
to find the distance between two points.
"""
from math import sqrt,pow
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return sqrt(pow((other.x-self.x),2)+pow((other.y-self.y),2))
if __name__=="__main__":
    print("POINT-1")
    x = int(input("Enter x Coordinate"))
    y = int(input("Enter y Coordinate"))
    ob1 = Point(x,y)
    print("POINT-2")
    x = int(input("Enter x Coordinate"))
    y = int(input("Enter y Coordinate"))
    ob2 = Point(x,y)
    print("DIFFERENCE BETWEEN TWO POINT = ",ob1-ob2)