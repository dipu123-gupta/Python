class DemoClass:
    v=20
# constructo
    def __init__(self):
        print("Hello Dosto")

    def showValue(self):
        self.c=self.v*self.v
        print(self.v)
        print(self.c)
    def showValue1(self,a,b):
        print("Wlecom to wscutech")
        print(a*b)


object=DemoClass()
object.showValue()
object.showValue1(20,40)