#function caching is used to store some function in cache so as to be fast
import time
from functools import lru_cache

@lru_cache(maxsize=3)#This we can set according to our needs
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == "__main__":
    print("Now running some work")
    some_work(3)
    print("Done.......calling it again")
    some_work(3) #This will not take 3 seconds again as with the help of lru_cache it will be stored in cache
    print("Done.......calling it again")
    some_work(3)