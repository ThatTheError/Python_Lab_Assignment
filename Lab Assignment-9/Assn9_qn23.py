"""
Write a program to convert the data of centigrade type to Fahrenheit type using class
object.
"""
class cenToFar:
    def __init__(self,cen):
        self.cen=cen
    def centofar(self):
        return self.cen*33.8
if __name__=="__main__":
    cen = float(input("Enter Centigrade : "))
    ob = cenToFar(cen)
    print(cen," CENTIGRADE = ",ob.centofar()," FARENHEIT")
