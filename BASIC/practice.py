
# def outer():
#   global glo
#   glo = 20
#   def inner():
#     global glo
#     glo = 30
#     print(glo)
# glo = 10
# outer()
# print( glo)

dicts = dict()
for l in enumerate(range(2)):
    dicts[l[0]] = l[1]
    dicts[l[1]+7] = l[0]
print(dicts)