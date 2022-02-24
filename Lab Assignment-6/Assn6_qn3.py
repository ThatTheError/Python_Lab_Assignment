"""3. Write a program that keeps name and phone numbers in a dictionary as key-value
pairs.
The program should display a menu that lets the user search a person’s phone, add a
new name and phone number, change an existing phone number, and delete an
existing name and phone number.     """

def search_phno():
  name = input("Enter the name of the fnd which phno you are looking for?")
  if name in phonebook:
    print("Number exist\n Number is :-",phonebook[name])
  else:
    print("Number doesnt exist")
def add_nm_no():
  nm=input("enter name : ")
  phno=int(input("Enter phno"))
  phonebook[nm]=phno
def change_no():
  nm=input("enter the name : ")
  phno=int(input("enter the new phno : "))
  phonebook[nm]=phno
def delete_no():
  name = input("Enter the name whose phone number you want to delete : ")
  del phonebook[name]
  print("After deletion")
  print(phonebook)
phonebook = {}
chh=1
def operation(choice):
  if choice==0:
    search_phno()
  elif choice==1:
    add_nm_no()
  elif choice==2:
    change_no()
  elif choice==3:
    delete_no()
  else:
    print("invalid choice")
    chh=-1
if __name__=="__main__":
  while chh>0:
    print("Enter your choice")
    ch=int(input("0. For search a Phnom \n1. Add name and no to phone book\n2. to change Phnom\n3. delete a Phnom\n"))
    operation(ch)
