list1 = []
largest=0
n = int(input("Enter the size of the list : "))
print("Enter the elements ")
for i in range(n):
    list1.append(input())
    if int(list1[i])>largest:
        largest = int(list1[i])
print("Largest = ",largest)

