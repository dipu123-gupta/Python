
class A:
    def displayA(self):
        print("Welcom to WsCubtech A")

class B(A):
    def displayB(self):
        print("Welcom to WsCubtech B")

class C(B):
    def displayC(self):
        print("Welcome to WsCubtech c")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()