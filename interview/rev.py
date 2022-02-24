class Stack:
    def __init__(self):
        self.top = -1
        self.stack = list()
    def push(self,word):
        self.top = self.top + 1
        self.stack.append(word)
    def pop(self):
        word = self.stack[self.top]
        self.top = self.top -1 
        return word
if __name__=="__main__":
    ob = Stack()
    name = input("Enter the string\n")
    for i in name:
        ob.push(i)
    for i in range(0,len(name)):
        print(ob.pop(),end="")