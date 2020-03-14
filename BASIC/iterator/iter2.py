#combinations(iterable,r)
from itertools import combinations

print(list(combinations(range(3),2)))
#OUT:
#this is different from permutation as that would have also given [(0,1)(1,0)]
print(list(combinations('abc',2)))

print(list(combinations('abc',3)))