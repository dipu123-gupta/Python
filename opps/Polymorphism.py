class Student:
    def displayinfo(self,name=""):
        print("Welcom to Wscubtech "+name)

class IIP(Student):
    def displayinfo(self, name=""):
        return super().displayinfo(name)
obj=Student()
obj.displayinfo()
obj.displayinfo("Dipu kumar")