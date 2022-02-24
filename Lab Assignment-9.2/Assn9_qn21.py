class Distance:
	def __init__(self,feet,inch):
		self.feet = feet
		self.inch = inch
	def __sub__(self,other):
		inchdiff = abs((self.feet*12+self.inch)-(other.feet*12+other.inch))
		return inchdiff//12,"FEET",inchdiff-((inchdiff//12)*12),"INCH"
if __name__=="__main__":
	print("INPUT-1")
	feet = int(input("Enter Feet\n"))
	inch = int(input("Enter inch\n"))
	ob1 = Distance(feet,inch)
	print("INPUT-2")
	feet = int(input("Enter Feet\n"))
	inch = int(input("Enter inch\n"))
	ob2 = Distance(feet,inch)
	print("DIFFERENCE = ",ob1-ob2)
