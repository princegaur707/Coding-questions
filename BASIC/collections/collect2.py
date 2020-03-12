#Deque from collections module
#It support append and remove from both the end
from collections import deque

d=deque()

d.append(1)
d.append(2)
d.append(3)

d.appendleft(4) #Similarly extendleft can also be used
d.appendleft(5)
d.appendleft(6)

print(d)
print(d.count(1))
d.clear()
print("After clearing:")
print(d)