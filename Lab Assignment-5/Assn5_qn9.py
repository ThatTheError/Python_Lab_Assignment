string = input("Enter a string : ")
list_str = string.split()
for i in list_str:
    word_list = i.split()
    print(word_list[0].capitalize(),end=" ")
    for i in word_list[1::]:
        print(i)
