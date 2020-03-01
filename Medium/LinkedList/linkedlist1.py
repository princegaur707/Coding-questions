#insert at last, delete first, view list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def deletefirst(self):
        if self.start==None:
            print("Linked list is empty")
        else:
            self.start=self.start.next#no need to use anything to delete as python automatically deletes anything which is not pointed anywhere
    def insertLast(self,value):
        newNode = node(value)
        if(self.start==None):
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def viewlist(self):
        if self.start==None:
            print("List is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
mylist=LinkedList()
mylist.insertLast(10)   
mylist.insertLast(20) 
mylist.insertLast(30)
mylist.insertLast(40)
mylist.insertLast(50) 
mylist.viewlist()
mylist.deletefirst()
print("\n")
mylist.viewlist()          
