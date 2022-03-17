ls = []
x = 1
while(x):
    n = int(input("Enter a no : "))
    ls.append(n)
    x = int(input("Enter 1 for continue 0 for exit"))
ls.sort()
print("Smallest = ",ls[0]," Largest = ",ls[-1])