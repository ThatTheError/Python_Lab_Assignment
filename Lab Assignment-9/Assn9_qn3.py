"""
3. Define a class for complex number with attributes real and imaginary, also include the
methods to add and subtract two different complex numbers and display them.
"""
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        self.comno = complex(real,img)
    def __add__(self, other):
        summ=self.comno+other.comno
        return summ
    def __sub__(self, other):
        subb = self.comno - other.comno
        return subb
if __name__=="__main__":
    print("Enter 1st complex no : ")
    real = int(input("Enter real\n"))
    img = int(input("Enter imaginary\n"))
    ob1 = Complex(real,img)
    print("Enter 2nd complex no : ")
    real = int(input("Enter real\n"))
    img = int(input("Enter imaginary\n"))
    ob2 = Complex(real,img)
    print("Addittion = ",ob1+ob2)
    print("Substraction = ",ob1-ob2)

