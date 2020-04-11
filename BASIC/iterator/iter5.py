#This showcases the difference of changing r and not changing of it
from itertools import combinations,chain 
test_str = "Geeks"
print("The original string is : " + str(test_str))
res = list(combinations(range(len(test_str) + 1), 2))
print(res) 
print("_____________________________________________________________________________________________________________________________________________________________________________________________")
str1="Geeks"
str1=list(str1)
print(list(chain.from_iterable(combinations([0,1,2,3,4,5],r) for r in range(len(str1)+1))))# as it is having 6 elements so powerset will have 64 tuples
