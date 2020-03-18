class node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class LinkedList:
    def __init__(self):
        self.start=None 
    def insert(self,value):
        newNode= node(value)
        if(self.start==None):
            self.start=newNode
        else:
            temp=self.start
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNode
    def delete(self):
        if(self.start==None):
            print("Linked list is empty!")
        else:
            self.start=self.start.next
    def view(self):
        if(self.start==None):
            print("Linked List is empty")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next

obj=LinkedList()
obj.delete()
obj.view()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.view()
obj.delete()
obj.view()
