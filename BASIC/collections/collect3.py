#Some more about deque:
from collections import deque

d=deque()

d.append(1)
d.append(2)
d.append(3)

d.extend('456') #This will append a,b,c while append would have considered abc as one element
d.append('456')
print(d)
d.extend([7,8,9,10]) #extend will even go inside the list and print iterables
d.append([7,8,9])
print(d)
d.remove(10) #remove only once and 1st occurence only
print(d)
print (d.pop())
print (d.popleft())
print(d)
d.rotate(-3) #rotate by 3 to the left
print(d)