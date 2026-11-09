# arithmetic operators
print("arithmetic operators")
a=20
b=5
# addition "+" 
print(a+b)
# subtraction "-"
print(a-b)
# multiplication "*"    
print(a*b)
# division "/"
print(a/b)
# modulus "%"
print(a%b)
# exponentiation "**"
print(a**b)
# floor division "//"
print(a//b)

# assignment operators
print("assignment operators")
x=10
print(x)
x+=5 # x=x+5
print(x)
x-=5 # x=x-5
print(x)
x*=5 # x=x*5 
print(x)
x/=5 # x=x/5
print(x)

# comparison operators return boolean values true or false
print("comparison operators return boolean values true or false")
c=10
d=20
print(c==d) # equal to "==" dono values same hai to true otherwise false
print(c!=d) # not equal to "!=" ager dono values same hai to false otherwise true
print(c>d)  # greater than ">" ager d se bada hoga to true otherwise false
print(c<d)  # less than "<" ager d se chota hoga to true otherwise false
print(c>=d) # greater than or equal to ">=" ager d se bara ya barabar hoga to true otherwise false
print(c<=d) # less than or equal to "<=" ager d se chota ya chhota barabar hoga to true otherwise false

# logical operators , ek se zyaada conditions ko check karne ke liye use hote hai
# example: x>10 and y<20, 
#          x>10 or y<20, 
#            not x>10
print("logical operators")
e=True
f=False
print(e and f) # logical and ,ager dono true hoga to true otherwise false
print(e or f)  # logical or , ager koi bhi true hoga to true otherwise false
print(not e)   # logical not , ager value true hoga to false otherwise true

# membership operators , ye check karte hai ki koi value kisi sequence me hai ya nahi
print("membership operators")
g=[1,2,3,4,5]
print(3 in g)   # in operator , agar value sequence me hai to true otherwise false
print(6 not in g) # not in operator , agar value sequence me nahi hai to true otherwise false

# identity operators , ye check karte hai ki koi variable kisi object ko point kar raha hai ya nahi
print("identity operators")
h=10
i=10
j=20
print(h is i) # is operator , agar dono variables same object ko point kar raha hai to true otherwise false
print(h is not j) # is not operator , agar dono variables same object ko point nahi kar raha hai to true otherwise false

# bitwise operators , ye operators binary numbers ke upar kaam karte hai
print("bitwise operators")
x=10 # binary 1010
y=8  # binary 1000
print(bin(x))
print(bin(y))
print("Result",bin(x & y)) # bitwise and , dono bits 1 hoga to 1