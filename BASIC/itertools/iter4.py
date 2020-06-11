# takewhile - takes items from an iterable while a predicate function remains true; exactly like filter
# chain - combines several iterables into one long one;
# accumulate - returns a running total of values in an iterable(sum total of iterables currently working on)

from itertools import chain, combinations #This is the way to make powerset

def powerset(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
print(list(powerset("abcd")))

print("______________________________________________________________________________________________________________________________________________")
from itertools import takewhile
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x%2==0, nums)
print(list(a))