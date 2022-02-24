list1 = []
n = int(input("Enter the size of the list : "))
print("Enter the elements ")
for i in range(n):
    list1.append(input())
print(list1[::-1])