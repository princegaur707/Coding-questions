#nametuple
#advantage: increase readability, it supports both access from key value and iteration(index), the functionality that dictionaries lack.
from collections import namedtuple

Student= namedtuple('Studnent',['name','age','rollno'])
student1= Student('A',22,1)
student2= Student('B',22,2)
student3= Student('C',22,3)

print("Name:",student1.name)
print("Age:",student1.age)
print("Roll No:",student1.rollno)