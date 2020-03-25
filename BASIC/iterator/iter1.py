from itertools import product
from itertools import permutations
from itertools import repeat

print(list(product([1,3,5],[2,5,6],[1,3,5])))

print(list(product([1,2,3],repeat=2))) #here 2 implies do product of 2 such lists

print(list(permutations([1,2,3],2)))# here 2 implies 2 elements at a time

print(list(permutations(range(3))))

print(list(permutations('abc',2)))#[('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]


# The function count counts up infinitely from a value.
#count has two arguments: count(x, y) where x is a start value and y is the increment/decrement pace (with y being a positive or negative number, respectively).
# The function cycle infinitely iterates through an iterable (for instance a list or string).
# The function repeat repeats an object, either infinitely or a specific number of times

for i in cycle("Huri"):
    print(i)

# Gimme a list which has "Huri" string 5 times
print(list(repeat("Huri", 5))