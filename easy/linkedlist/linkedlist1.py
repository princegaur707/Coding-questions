#insert at last, delete first,delete last view list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.start=None
    def insert(self,value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNode
    def deletefirst(self):
        if self.start==None:
            print("Linked list is empty!")
        else:
            self.start=self.start.next  #no need to use anything to delete as python automatically deletes anything which is not pointed anywhere
    def deletelast(self):
        if self.start==None:
            print("Linked list is empty!")
        if self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def viewlist(self):
        if self.start==None:
            print("Linked list is empty!")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data, end=" ")
                temp=temp.next   
obj=linkedlist()  
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.viewlist()
print("\n")
obj.deletefirst()
obj.viewlist()
print("\n")
obj.deletelast()
obj.viewlist()     
