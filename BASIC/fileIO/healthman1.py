def getdate():
    import datetime
    return datetime.datetime.now()
ch=int(input("Enter your choice\n\t\t(0-add 1-view): "))
a=input("Enter your name: ")
print(getdate()) 
if(ch==0):
    if(a=="prince"):
        with open ("prince.txt",'a') as pri:
            value=input("Type here: ")
            content=pri.write(str(getdate())+":"+value+"\n")
    elif(a=="abhishek"):
        with open ("abhi.txt") as ab:
            value=input("Type here: ")
            content=ab.write(str(getdate())+":"+value+"\n")
    elif(a=="ishjot"):
        with open ("ish.txt") as isa:
            value=input("Type here: ")
            content=isa.write(str(getdate())+":"+value+"\n")

else:
    print(getdate())  
    if(a=="prince"):
        with open ("prince.txt") as pri:
            content=pri.readlines()
            print("\n".join(content))
    elif(a=="abhishek"):
        with open ("abhi.txt") as ab:
            content=ab.readlines()
            print("\n".join(content))
    elif(a=="ishjot"):
        with open ("ish.txt") as isa:
            content=isa.readlines()
            print("\n".join(content))
