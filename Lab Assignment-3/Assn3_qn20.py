row = int(input("Enter the row size : "))
no = 1
for i in range(row):
    for j in range(i+1):
        print(no," ",end='')
        no+=1
    print()
