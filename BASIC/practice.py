l=10
def function1():
    global l
    l=l+45
    print(f"in function{l}")
    print(l)
print("Before calling")
print(l)
function1()
print("After calling")
print(l)
# glo = 10
# outer()
# print( glo)
#{0:1,8:0}
# dicts = dict()
# for l in enumerate(range(2)):
#     print (dicts)
#     print ("\n")
#     dicts[l[0]] = l[1]
#     dicts[l[1]+7] = l[0]
#     print (l[0],l[1])
# print(dicts)
# dig = 0
# for i in range(0.0, 5.0, 0.1)
#     dig += i
#     i+=0
# print(dig)