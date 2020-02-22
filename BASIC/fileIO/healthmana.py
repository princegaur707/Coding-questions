def getdate():
    import datetime
    return datetime.datetime.now()
a=input("Enter your name: ")
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