#Counter
#https://www.codechef.com/submit/LAPIN : counter will just see if the count of every element is same ( it will also consider 0 count too)
from collections import Counter

print("1________________________________________________________________________________________")
c=Counter("BAAAAAllahabad")
print(c) #elements are arranged in decreasing order of frequency(if frequency is same then  order of occurrence)
#in form of dictionary with frequency as a value
print("2________________________________________________________________________________________")

for i in c.elements():
    print(i,end=" ")   #will print all elements after clubing together all multiple occurrences sorting on the basis of position
print("\n3________________________________________________________________________________________")

print(c.elements())#It prints a location because it returns an itertool, not a specific data-container.
print("4________________________________________________________________________________________")

print(list(c.elements()))
print("5________________________________________________________________________________________")

x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3) 
for i in x.elements(): 
    print( "% s : % s" % (i, x[i]), end ="||") 
print("\n________________________________________________________________________________________")
#If the count of an item is already initialized in Counter object, then it will ignore the ones with zero and negative values