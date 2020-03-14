#Counter
from collections import Counter

print("________________________________________________________________________________________")
c=Counter("Allahabad")
print(c) #elements are arranged in decreasing order of frequency(if frequency is same then  order of occurrence)
#in form of dictionary with frequency as a value
print("________________________________________________________________________________________")

for i in c.elements():
    print(i,end=" ")
print("\n________________________________________________________________________________________")

print(c.elements())#It prints a location because it returns an itertool, not a specific data-container.
print("________________________________________________________________________________________")

print(list(c.elements()))
print("________________________________________________________________________________________")

x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3) 
for i in x.elements(): 
    print( "% s : % s" % (i, x[i]), end ="||") 
print("\n________________________________________________________________________________________")
#If the count of an item is already initialized in Counter object, then it will ignore the ones with zero and negative values