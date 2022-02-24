name = input("Enter the Name : ")
print(name[0],end='')
for i in range(len(name)):
    if name[i]==' ':
        print('.',name[i+1],end='')
