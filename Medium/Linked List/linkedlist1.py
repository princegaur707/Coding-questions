#insert at last
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def insertLast(self,value):
        newNode = node(value)
        if(self.start=None):
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
