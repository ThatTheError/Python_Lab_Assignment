class Stack:
    def __init__(self):
        self.top = -1
        self.stack = list()
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def insertion(self,val):
        self.top = self.top+1
        self.stack.append(val)
        print(str(self.stack[self.top])+" Inserted sucessfully")
        return
    def deletion(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(str(self.stack[self.top])+" Deleted Sucessfully")
            self.top -= 1
    def printing(self):
        temp = self.top
        while temp >= 0 :
            print(self.stack[temp]," ",end = " ")
            temp -= 1
if __name__=="__main__":
    ob = Stack()
    x=1
    while x>0:
        ch = int(input("1.Insertion\n2.Deletion\n3.Print Stack\n"))
        if ch==1:
            val = int(input("Enter value to insert\n"))
            ob.insertion(val)
        elif ch==2:
            ob.deletion()
        elif ch==3:
            ob.printing()
        elif ch==0:
            x=0
        else:
            print("Invalid choice")