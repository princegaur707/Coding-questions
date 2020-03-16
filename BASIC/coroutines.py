#coroutine: To save the time to run the heavey task again and again
#https://www.geeksforgeeks.org/coroutine-in-python/
def searcher():
    import time
    # some 4 second time consuming task
    book="let's make this world livable not earnable"
    time.sleep(5)

    while True: #from 2nd time it will run from here directly
        try:
            text=(yield) #yield (give away) control periodically or when idle in order to enable multiple applications to be run simultaneously
            if text in book:#whatever value we send to coroutine is captured and returned by (yield) expression
                print("Your text in the book")
            else:
                print("Your text not in the book")
        except GeneratorExit:
            print("Closing coroutine")

object1=searcher()#creates instance of subroutine
print("Wait! Training and reading will take 5 seconds.............")
next(object1) #this is running that above code containing 5 seconds
print("Done...")
inp1=input("Enter the string to be searched: ")
#object1.__next__()
object1.send(inp1) #A value can be send to the coroutine by send() 
input("Search any key to continue:   ")
inp2=input("Enter the string to be searched: (See the line 5 second one will not come) ")
#object1.__next__()
object1.send(inp2) #this search will take very less time as now it is running from while loop directly
object1.close() #After closing coroutine, now it will free resources and if we try to send values, it will raise StopIteration exception.