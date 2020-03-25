import re
#findall,search,split,sub,finditer
#rawstring: Takes the string as it is given do not consider escape sequence character(\n) etc
mystr="""Data structuresDeclaring different data types:
List:                  x=[] or x= list()
Tuple :             x=() or x= tuple()
Dictionary :     x={} or x=dict()
Set:                   x= set()
String:              x=”” or x= str()

List:
Two ways of accessing list values forward and backward indexing:
[ “python” ,12 , 2.0 , “movie” ]
Forward indexing : 0,1,2,3
Backward indexing : -4,-3,-2,-1
[ start : end : step ]

Functions supported:

1.	append( object )
2.	count( object )
3.	extend( list )
4.	index( object )
5.	insert( index , object )
6.	pop( object ): pop(2)  represents element at 2nd  index position by default it pops last one
7.	remove(object ): asks which value is to be removed ->do not work for string(use replace instead) works single time 
8.	reverse()
9.	sort()
10.	Map(): space separated input


Dictionary:
KEYS() :  returns sequence of dictionary keys in tuple
values() :  returns sequence of dictionary values in tuple
items():   returns sequence of ( keys , values )
clear():   deletes all entries in dictionary
get( key ):   returns the value for the KEY

Important Notes:
Python package index
Int(‘111’,2) –> 7
Int(‘a’,16) –>  10 
prince
""" #multiline string declaration
pattern=re.compile(r'e$') # $ matches the end
matches= pattern.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[1160:1165])