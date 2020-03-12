from collections import deque

d=deque()

d.append(1)
d.append(2)
d.append(3)

d.extend('abc') #This will append a,b,c while append would have considered abc as one element
d.append('abc')
print(d)
d.extend([4,5,6]) #extend will even go inside the list and print iterables
d.append([4,5,6])
print(d)
d.remove(1)
print(d)
print (d.pop())
print (d.popleft())