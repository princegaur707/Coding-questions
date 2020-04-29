class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.start=None
    def insert(self,value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def middle(self):
        if self.start==None:
            print("Linked list is empty!")
        else:
            temp=temp1=self.start
            while(temp.next!=None):
                temp=temp.next.next
                temp1=temp1.next
            print("Middle is :",temp1.data)
    def viewlist(self):
        if self.start==None:
            print("Linked list is empty!")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data, end=" ")
                temp=temp.next   
obj=Linkedlist()  
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.middle()
obj.viewlist()    
