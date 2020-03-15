"""
iterable : python object in which __iter__() or __getitem__() is defined
iterator: python object in which __next__() is defined
iteration :
generators are those iterators which can be traversed single time
eg: when we run loop it generates values on the fly not stores and print
Advantage:Saves memory(If we don't want to store any large no. to be saved in our system and then printed)
""" 
def gen(n):
    for i in range(n):
        yield i
g=gen(987654321)
print(g)