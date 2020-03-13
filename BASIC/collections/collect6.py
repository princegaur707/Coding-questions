#Default Dict
#advantage: It do not shows error if unknown key valued asked for,faster
from collections import defaultdict

d=defaultdict(lambda :"Default Value")
d['name']='prince'
d['age']=22

print(d['name'])
print(d['age'])
print(d['height'])