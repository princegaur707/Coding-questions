from itertools import product
from itertools import permutations

print(list(product([1,3,5],[2,5,6],[1,3,5])))

print(list(product([1,2,3],repeat=2))) #here 2 implies do product of 2 such lists

print(list(permutations([1,2,3],2)))# here 2 implies 2 elements at a time

print(list(permutations(range(3))))

print(list(permutations('abc',2)))#[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]