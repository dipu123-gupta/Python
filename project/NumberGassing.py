import random

Cnumber = random.randrange(1,101)

userInput=int(input("Enter Your number:--"))
if userInput>Cnumber:
    print("Computer number",Cnumber)
    print("Your guess number is too high")
elif userInput<Cnumber:
    print("Computer number",Cnumber)
    print("Your guess Number is too low")
else:
    print("Computer number",Cnumber)
    print("Your guess number is equal")