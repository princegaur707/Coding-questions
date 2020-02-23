l1=['A','B','C','D','E']
print(list(enumerate(l1)))
print("-----------------------------------------")
for item in enumerate(l1):
    print(item)
print("-----------------------------------------")
for index,item in enumerate(l1):
    print(index,item)
print("-----------------------------------------")
#Printing even index elements
for index,item in enumerate(l1):
    if index%2==0:
        print(item)