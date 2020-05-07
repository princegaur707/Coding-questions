#combinations(iterable,r)
from itertools import combinations,combinations_with_replacement,permutations

print(list(combinations(range(3),2)))
print(list(permutations(range(3),2)))
#OUT:[(0, 1), (0, 2), (1, 2)]  range(3): 0,1,2 elements to be used ---- 2: with 2 elements in one 
#this is different from permutation as this is also giving [(0,1)(1,0)]
print("______________________________________________________________________________________________________________________________________________")
print(list(combinations('abc',2)))
print("______________________________________________________________________________________________________________________________________________")
print(list(combinations('abc',3)))
print("______________________________________________________________________________________________________________________________________________")
print(list(combinations_with_replacement(range(3),2)))#Repetition is allowed 
print("______________________________________________________________________________________________________________________________________________")
print(list(combinations_with_replacement('abc',2)))
print("______________________________________________________________________________________________________________________________________________")
print(list(combinations_with_replacement('abc',2))) # it will allow ('a','a') also
