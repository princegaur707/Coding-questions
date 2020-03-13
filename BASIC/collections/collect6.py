#Default Dict
#advantage: Do not shows key error instead shows default message ,faster
from collections import defaultdict

d=defaultdict(lambda :"Default Value")  #known as default factory attribute
d['name']='prince'
d['age']=22

print(d['name'])
print(d['age'])
print(d['height'])
print("________________________________________________________________________________________")
#Storing every key with its value in new dictionary with value as list
s=[('Red',5),('Blue',6),('White',3),('Blue',2)]
d=defaultdict(list)

for i,j in s:
    d[i].append(j)
print(d)
print(d.items())
print("________________________________________________________________________________________")
#Finding occurence of each element
string="mississippi"
d=defaultdict(int)
for i in string:
    d[i]+=1
print(d.items()) 