def func1():
    x=20
    def func2():
        global x
        x=88
    print(f"Before calling: {x}")
    func2()
    print(f"After calling: {x}")
func1()
print(f"Outside : {x}")