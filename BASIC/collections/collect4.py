#Counter
from collections import Counter

c=Counter("Allahabad")
print(c) #elements are arranged in decreasing order of frequency
print("________________________________________________________________________________________")
for i in c.elements():
    print(i,end=" ")
print("\n________________________________________________________________________________________")
print(c.elements())#-> It will print garbage value when directly printed because it returns an itertool, not a specific data-container.
print("________________________________________________________________________________________")
x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3) 
print(list(c.elements()))
print("________________________________________________________________________________________")
for i in x.elements(): 
    print( "% s : % s" % (i, x[i]), end ="||") 
#If the count of an item is already initialized in Counter object, then it will ignore the ones with zero and negative values.