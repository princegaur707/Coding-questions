from itertools import product
from itertools import permutations

print(list(product([1,3,5],[2,5,6])))

print(list(product([1,3,5],repeat=2)))

print(list(permutations(range(3))))

print(list(permutations([1,2,3],2)))# here 2 implies 2 elements at a time

print (list(permutations('abc',2)))#[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]