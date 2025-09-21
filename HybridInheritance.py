#Multilevel Inheritance
class A:
    def func1(self):
        print("This is func1 from class A")
class B(A):
    def func2(self):
        print("This is func2 from class B")
class C(B):
    def func3(self):
        print("This is func3 from class C")
obj=C()
obj.func1()
obj.func2()
obj.func3()

#Converting above Multilevel Inheritance into Hybrid Inheritance
class A:
    def func1(self):
        print("This is func1 from class A")
class B(A):
    def func2(self):
        print("This is func2 from class B")
class D:
    def func(self):
        print("This is func from class D")
class C(B,D):
    def func3(self):
        print("This is func3 from class C")
obj=C()
obj.func1()
obj.func2()
obj.func3()
obj.func()

    