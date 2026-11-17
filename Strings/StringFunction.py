w="welcome to my world"

lower=w.lower()

print(lower)

Upper=w.upper()
print(Upper)

title=w.title()
print(title)

c=w.capitalize()
print(c)

print(w.find("e",2))

print(w.index("w",3))

name="dipukumar"

print(name.isalpha())

digi="98590"

print(digi.isdigit())

a="jflkjdfn12334"

print(a.isalnum())

a=65

print(chr(a))

h='H'
print(ord(h))

w="welcome {} to {} my world".format("hi",20)
print(w)

a="hello{0} kumar {1} welcome".format("Dipu",30)
print(a)


c="Welcom {b:>10} to {a}Wscubtech".format(a=30,b=40)
print(c)

c="Welcom {b:<10} to {a}Wscubtech".format(a=30,b=40)
print(c)

c="Welcom {b:^10} to {a}Wscubtech".format(a=30,b=40)
print(c)

