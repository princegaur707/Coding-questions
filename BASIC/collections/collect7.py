#nametuple
#advantage: increase readability, it supports both access from key value and iteration(index), the functionality that dictionaries lack.
from collections import namedtuple

Student= namedtuple('student',['name','age','rollno'])
student1= Student('A',22,1)
student2= Student('B','22',2)#accepting string as well as int
student3= Student('C',22,3)

print("Name:",student1.name) #here it is possible to give name as a parameter not necessarily index value
print("Age:",student1.age)
print("Roll No:",student1.rollno)

print(student1._fields)
print(student2._replace(name='D'))