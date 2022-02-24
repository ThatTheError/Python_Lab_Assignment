string = input("Enter a sentence : ")
word_list = string.split()
word = input("Enter the word you want to delete : ")
for i in word_list:
    if i == word:
        word_list.remove(i)


