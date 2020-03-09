def func1(d):
    print("1")
    d()
    print("3")
def d():
    print("2")
func1(d)

# def executor(func):
#     print(func([1,2,3]))
# executor(sum)
# def function1():
#     print("Inside 1")
#     def function2():
#         print("Inside 2")
#         def function3():
#             print("Inside 3")
#         function3()
#     function2()
        
# function1()
#function2() 
#function3()   these lines cause error as the function is being called out of its range
