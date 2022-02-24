"""
5. Write a program that accepts a string and change its lowercase vowels to special
character as given below:
a #
e @
i $
o %
u !
"""

str1=input("enter a string ")
str1=str1.lower()
list1=list(str1)
spldict={'a':'#','e':'@','i':'$','o':'%','u':'!'}
for i in list1:
  if i in spldict:
    print(spldict[i],end=' ')
  else:
    print(i,end=' ')