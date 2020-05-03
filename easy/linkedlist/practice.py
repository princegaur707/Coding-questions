class Stack:
    def __init__(self,maxsize):
        self.top=-1
        self.maxsize=maxsize
        self.stack=[0]*maxsize
    
    def isfull(self):
        if self.top>self.maxsize-1:
            print("Stack overflow!")
            return True
        print("Stack is not full!")
        return False

    def isempty(self):
        if self.top<0:
            print("Stack underflow!")
            return True
        print("\nStack in not Empty!")
        return False
    
    def push(self,value):
        if self.isfull():
            return False
        else:
            self.top+=1
            self.stack[self.top]=value
            return True
    
    def pop(self):
        if self.isempty():
            return False
        else:
            var=self.stack[self.top]
            self.top-=1
            print("pop number:",var)
            return var
    
    def peek(self):
        if self.isempty():
            return False
        else:
            return self.stack[self.top]
     
    def view(self):
        if self.isempty():
            return False
        else:
            temp=self.top
            while temp!=-1:
                print(self.stack[temp],end=" ")
                temp-=1

obj=Stack(5)
obj.push(1);obj.push(2);obj.push(3),obj.push(4),obj.push(5);obj.view()
obj.pop();obj.view()
print(obj.peek())