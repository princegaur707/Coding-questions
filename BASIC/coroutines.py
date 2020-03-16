def searcher():
    import time
    # some 4 second time consuming task
    book="let's make this world livable not earnable"
    print("This work taking 3 seconds")
    time.sleep(3)
    while True:
        text=(yield)
        if text in book:
            print("Your text in the book")
        else:
            print("Your text not in the book")

search=searcher()#creates instance of subroutine
next(search)
inp1="Enter the string to be searched: "
search.send(inp1)
input("Search any key to continue:   ")
inp2="Enter the string to be searched: "
search.send(inp2) #this search will take very less time as 