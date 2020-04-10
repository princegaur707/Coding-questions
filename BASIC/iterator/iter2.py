#combinations(iterable,r)
from itertools import combinations,combinations_with_replacement

print(list(combinations(range(3),2)))
#OUT:[(0, 1), (0, 2), (1, 2)]  range(3): 0,1,2 elements to be used ---- 2: with 2 elements in one 
#this is different from permutation as that would have also given [(0,1)(1,0)]
print(list(combinations('abc',2)))

print(list(combinations('abc',3)))

print(list(combinations_with_replacement(range(3),2)))
#Repetition is allowed 

print(list(combinations_with_replacement('abc',2)))

print(list(combinations_with_replacement('abc',2))) # it will allow ('a','a') also