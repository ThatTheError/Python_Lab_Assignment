"""
1. Define the class BankAccount, which has the attribute balance & it is initialized during
object creation. The class also has the methods for depositing the amount, for
withdrawing the amount & checking the balance. Use menu-based approach to ask the
user for selecting a operation.
"""
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposite(self):
        amt = int(input("Enter Amount to deposite\n"))
        self.balance+=amt
    def withdraw(self):
        amt = int(input("Enter withdraw amount\n"))
        self.balance-=amt
    def checkBalance(self):
        print("ACCOUNT BALANCE = ",self.balance)
if __name__=="__main__":
    bal = int(input("Enter Minimum Amount to create Account\n"))
    ob = BankAccount(bal)
    while True:
        print("Enter Your Choice")
        ch = int(input("1.DEPOSITE\n2.WITHDRAW\n3.CHECK_BALANCE\n4.EXIT\n"))
        if ch==1:
            ob.deposite()
        elif ch==2:
            ob.withdraw()
        elif ch==3:
            ob.checkBalance()
        elif ch==4:
            break
        else:
            print("Invalid Chice!")
