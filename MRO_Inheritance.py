#MRO-Method Resolution Order 
class A: pass
class B(A): pass
class C(B): pass
print(C.mro())

#MRO
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):
    pass
obj=D()
obj.show()
print(D.mro())