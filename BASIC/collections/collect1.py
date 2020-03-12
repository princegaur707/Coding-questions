#An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted
#Key value Change: If the value of a certain key is changed, the position of the key remains unchanged in OrderedDict.
#Deletion and Re-Inserting: Deleting and re-inserting the same key will push it to the back as OrderedDict however maintains the order of insertion.
from collections import OrderedDict

OrderedDict1=OrderedDict()
OrderedDict1['name']="Prince"
OrderedDict1['nationality']="Indian"
OrderedDict1['age']=22
print(OrderedDict1)

#Normal Dictionary
Ordinarydict1={}
Ordinarydict1['name']="Prince"
Ordinarydict1['nationality']="Indian"
Ordinarydict1['age']=22
print(Ordinarydict1)

#Two normal dictionaries will be equal if they have same key values pair but different sequence
#Two ordered dictonaries will not be equal even if they have same key value pair but not same sequence