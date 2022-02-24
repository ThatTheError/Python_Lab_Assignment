"""
Write a program to convert the data of kilometer type to meter type using class object.
"""

class kmToMtr:
    def __init__(self,km):
        self.km = km
    def kmtomtr(self):
        return self.km*1000
if __name__=="__main__":
    km = int(input("Enter KM : "))
    ob = kmToMtr(km)
    print(km," KM = ",ob.kmtomtr()," METER")