print('''
+ Add
- Subtract
* Multiply
/ Divide
% Modulus
''')
num1=int(input("Enter first number1: "))
num2=int(input("Enter second number2: "))
opr = input("Enter operator: ")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="%":
    print(num1%num2)
else:
    print("invalid operatin")