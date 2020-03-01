#delete furst node
class node:
    def __init__(self,data):
        self.data=data
        self.next=None;
class LinkedList:
    def __init__(self):
        self.start=None;
    def deletefirst(self):
        if self.start==None:
            print("Linked list is empty")
        else:
            self.start=self.start.next#no need to use anything to delete as python automatically deletes anything which is not pointed anywhere
    def insertlast(self,value):
        newNode= node(value)
        if(self.start==None):
            self.start=newNode   
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def view(self):
        if(self.start==None):
            print("list is empty")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
nlist=LinkedList()
nlist.insertlast(1)
nlist.insertlast(2)
nlist.insertlast(3)
nlist.insertlast(4)
nlist.view()
print("\n")
nlist.deletefirst()
nlist.view()