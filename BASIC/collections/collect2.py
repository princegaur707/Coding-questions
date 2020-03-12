#Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container,
#  as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
# 1. append() :- This function is used to insert the value in its argument to the right end of deque.
# 2. appendleft() :- This function is used to insert the value in its argument to the left end of deque.
# 3. pop() :- This function is used to delete an argument from the right end of deque.
# 4. popleft() :- This function is used to delete an argument from the left end of deque.
# 5. index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
# 6. insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
# 7. remove() :- This function removes the first occurrence of value mentioned in arguments.
# 8. count() :- This function counts the number of occurrences of value mentioned in arguments.

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