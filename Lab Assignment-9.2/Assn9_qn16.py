class ComplexNumber:
	def __init__(self,real,img):
		self.real = real
		self.img = img
		self.comno = complex(real,img)
	def __add__(self,other):
		res = self.comno+other.comno
		return res
	def __sub__(self,other):
		res = self.comno-other.comno
		return res
if __name__=="__main__":
	print("1st Number : ")
	real = int(input("Enter real \n"))
	img = int(input("Enter imaginary \n"))
	ob1 = ComplexNumber(real,img)
	print("2nd Number : ")
	real = int(input("Enter real \n"))
	img = int(input("Enter imaginary \n"))
	ob2 = ComplexNumber(real,img)
	print("ADDITION = ",ob1+ob2)
	print("SUBSTRACTION = ",ob1-ob2)