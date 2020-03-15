"""
iterable : python object in which __iter__() or __getitem__() is defined
iterator: python object in which __next__() is defined
iteration :
generators are those iterators which can be traversed only once
eg: when we run loop it generates values on the fly not stores and print
Advantage:Saves memory(If we don't want to store any large no. to be saved in our system and then printed)
https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/
""" 
def gen(n):
    for i in range(n):
        yield i # yield is like return but it returns generator
g=gen(3)
print(g)
print(g.__next__())#here it is printing yield values(which are ready as generator object)
print(g.__next__())
h="harry"
ier=iter(h)
print(ier.__next__())
print(ier.__next__())
