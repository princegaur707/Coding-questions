#decorators:
# In Python, functions are the first class objects, which means that –
# Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
# Functions can be defined inside another function and can also be passed as argument to another function.
def func1(d):
    def func2():
        print("1")
        d()
        print("3")
    return func2
@func1
def d():
    print("2")
#d=func1(d) [@ is the alternative of this line (function is being return as an argument)]
d()

def executor(func):
    print(func([1,2,3]))
executor(sum)

def function1():
    print("Inside 1")
    def function2():
        print("Inside 2")
        def function3():
            print("Inside 3")
        function3()
    function2()
        
function1()
# function2()   this lines cause error as the function is being called out of its range
    # function3()   this lines cause error as the function is being called out of its range
