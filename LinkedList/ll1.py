class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertion(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        else:
            temp1 = self.head
            while temp1.next is not None:
                temp1 = temp1.next
            temp1.next = newNode
            return
    def deletion(self):
        temp = self.head
        if temp is None:
            print("List is Empty")
            return
        elif temp.next is None:
            self.head = None
            temp=None
            return
        else:
            self.head = self.head.next
            return
    def printing(self):
        temp = self.head
        while temp.next is not None:
            print(str(temp.val)+"->",end=" ")
            temp = temp.next
        print(temp.val)

if __name__=="__main__":
    ob = LinkedList()
    x=1
    while x>0:
        ch = int(input("1.Insert node\n2.Delete a node\n3.Print list\n"))
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