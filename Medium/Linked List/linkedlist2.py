#delete furst node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None;
class LinkedList:
    def __init__(self):
        self.start=None;
    def deleteFirst(self):
        if self.start==None:
            print("Linked list is empty")
        else:
            temp=self.start
            self.start=self.start.next
    def insertLast(self,value):
        newNode= node(value)
        if(self.start==None):
            self.start=newNode   
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next