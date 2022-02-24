list1 = []
n = int(input("Enter the size of the list : "))
print("Enter the elements ")
for i in range(n):
    list1.append(input())
x = list1[n-1]
for i in range(n-1,0,-1):
    list1[i] = list1[i-1]
list1[0] = x
print(list1)