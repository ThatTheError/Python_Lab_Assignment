class Queue:
    def __init__(self):
        self.front = -1 
        self.rear = -1
    def insertion(self,val):
        

    def deletion(self):
        if self.front and self.rear == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
    def printing(self):
        pass

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