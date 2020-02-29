# strs = ['aa', 'BB', 'zz', 'CC']
#   print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
#   print sorted(strs, reverse=True)   ## ['zz', 'aa', 'CC', 'BB']

# strs = ['ccc', 'aaaa', 'd', 'bb']
#   print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']

a=['aab','a','ab','b','abb','aba','acc']
a=sorted(a)
#a=sorted(a,key=len)
print(a)
a=sorted(a,key=len)
#a=sorted(a)
print(a)