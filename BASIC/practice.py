class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.start=None
    def insert(self,value):
        newnode=node(value)
        if(self.start==None):
            self.start=newnode
        else:
            temp=self.start
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def view(self):
        if(self.start==None):
            print("linked list is empty")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
    def deletefirst(self):
            if(self.start==None):
                print("Linied list is empty")
            else:
                self.start=self.start.next
nlist=LinkedList()
nlist.insert(10)
nlist.insert(20)
nlist.insert(30)
nlist.view()
print("\n")
nlist.deletefirst()
nlist.view()

# glo = 10
# outer()
# print( glo)
#{0:1,8:0}
# dicts = dict()
# for l in enumerate(range(2)):
#     print (dicts)
#     print ("\n")
#     dicts[l[0]] = l[1]
#     dicts[l[1]+7] = l[0]
#     print (l[0],l[1])
# print(dicts)
# dig = 0
# for i in range(0.0, 5.0, 0.1)
#     dig += i
#     i+=0
# print(dig)