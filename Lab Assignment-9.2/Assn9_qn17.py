class Matrix:
	def __init__(self,mat):
		self.mat = mat
	def __add__(self,other):
		for i in range(row):
			for j in range(col):
				self.mat[i][j]=self.mat[i][j]+other.mat[i][j]
		return self.mat	
if __name__=="__main__":
	row = int(input("Enter size of the row"))
	col = int(input("Enter size of the column"))
	matrix = []
	print("INPUT-1\nEnter the matrix value")
	for i in range(row):
		mat1=[]
		for j in range(col):
			mat1.append(int(input()))
		matrix.append(mat1)
	ob1 = Matrix(matrix)
	matrix = []
	print("INPUT-2\nEnter the matrix value")
	for i in range(row):
		mat2=[]
		for j in range(col):
			mat2.append(int(input()))
		matrix.append(mat2)
	ob2 = Matrix(matrix)
	print("RESULT = ",ob1+ob2)
