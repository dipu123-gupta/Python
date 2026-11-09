# variables are used to store data in memory
a=10

b=70
# printing the values of a and b
print(a,b)
# printing the memory address of a and b or ager dono variables ka same hoga to ek hi memory address hoga
print(id(a),id(b))

print("a",b)
#  storeing string values in variables and variables c and d are pointing to the same string object in memory
c="hello"
d="hello"
# printing the values of c and d
print(c)
print(d)
print(id(c),id(d))

# strings concatination
e="hello"
f="world"
print(e+" "+f)

g=30
# print(g+f) # this will give error because we are trying to add integer and string   