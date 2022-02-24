list1 = []
n = int(input("Enter the size of the list : "))
print("Enter the elements ")
for i in range(n):
    list1.append(input())
    if int(list1[i])%2 != 0:
        list1[i] = int(list1[i])*3
    else:
        list1[i] = int(list1[i])//2
print(list1)
