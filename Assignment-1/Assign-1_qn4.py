import random
integerList = list()
def rlist(n):
    for i in range(n):
        no = random.randint(51,151)
        integerList.append(no)
n = int(input("Enter the size of the integer list : "))
rlist(n)
print(integerList)
integerList.sort()
print("Top 3 element of the list = ")
for i in integerList[:-4:-1]:
    print(i," ",end= " ")