i = '(a,a),(b,b),(c,c),(d,d)'#converting this to [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')]

l = []

for tup in i.split('),('):   #considering all 3 i.e, ) , ( as parameters to split
    #tup looks like `(a,a` or `b,b`
    #print(f"first     {tup}")
    tup = tup.replace(')','').replace('(','')
    #print(f"second    {tup}")
    #tup looks like `a,a` or `b,b`
    l.append(tuple(tup.split(',')))
    print(l)

print(l)
