""" 2. Write a program that reads a string from keyboard and prints the unique words.
Your program should convert input string to lower case. """

str1 = input("enter a string ")
str1=str1.lower()
x=str1.split(' ')
x1=[]
for i in x:
  if i not in x1:
    x1.append(i)
dictstr={i:x1[i] for i in range(len(x1))}
#print(dictstr)
print(len(dictstr))
res = "".join(str(i+" ") for i in dictstr.values())
print(res)
"""
def to_capital():
  string = input("Enter a string : ")
  list_str = string.split()
  for i in list_str:
    word_list = i.split()
    print(word_list[0].capitalize(),end=" ")
    for i in word_list[1::]:
        print(i)

to_capital()    """