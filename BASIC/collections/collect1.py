#An OrderedDict is a dictionary subclass that remembers the order in which keys were inserted
#Key value Change: If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.
#Deletion and Re-Inserting: Deleting and re-inserting the same key will insert it at last.
from collections import OrderedDict

OrderedDict1=OrderedDict()
OrderedDict1['name']="Prince"
OrderedDict1['nationality']="Indian"
OrderedDict1['age']=22
OrderedDict1['name']="Prince Gaur"
print(OrderedDict1)

#print(type(OrderedDict1))

#Normal Dictionary
Ordinarydict={}
Ordinarydict['name']="Prince"
Ordinarydict['nationality']="Indian"
Ordinarydict['age']=22
Ordinarydict['name']="Prince Gaur"
print(Ordinarydict)

#Two normal dictionaries will be equal if they have same key values pair but different sequence
#Two ordered dictonaries will not be equal even if they have same key value pair but not same sequence