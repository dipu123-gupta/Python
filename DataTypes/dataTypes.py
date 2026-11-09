# Data Types in Python
# there two types of data types in python
# 1. mutable data types -> list, dict, bytearray
# 2. immutable data types -> int, float, string, tuple, set,complexs

# numeric data types
# integers, float, complex numbers
a=10 # -> int data type
print(a,"is of type",type(a))
a=20.0 # -> float data type
print(a,"is of type",type(a))
a=(2+2j) # -> complex data type
print(a,"is of type",type(a))

# string data type -> string is a sequence of characters enclosed in single or double quotes 
b="Hello, World!"
print(b,"is of type",type(b))
c='Python'
print(c,"is of type",type(c))

s='''
hello
welcom to my code hub
'''
print(s,"is of type",type(s))

# list data type -> list is a collection of items which is ordered and changeable. Allows duplicate members.and it is most of used data type in python and flexible data type
d=[1,2,3.3,"hello",True,False]

d[2]=3.5 # changeable
print(d,"is of type",type(d))

# tuple data type -> tuple is a collection of items which is ordered and unchangeable. Allows duplicate members.
e=(1,2,3.3,"hello",True,False)
print(e,"is of type",type(e))

t=(10)
print(t,"is of type",type(t)) # it is not a tuple because it is not enclosed in parenthesis

# Dictionary data type -> dictionary is a collection of items which is unordered, changeable and indexed. No duplicate members. in python dictionary is written with curly brackets, and it has keys and values.
f={
   "name":"John",
   "age":30,
   "city":"New York"
   }
f["name"] = "Jane" # changeable
print(['name'])
print(f,"is of type",type(f))
