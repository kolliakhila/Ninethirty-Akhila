#single inheritance
class Teacher:
    def teach(self):
        print("Iam the Teacher of this subject")
class Student(Teacher):
    def learn(self):
        print("This is my favorite subject")
obj=Student()
obj.learn()
obj.teach()
obj2=Teacher()
obj2.teach()

#multilevel inheritance
class Animal:
    def func1(self):
        print("This is the Parent class")
class Dog(Animal):
    def func2(self):
        print("This is the child class of Animal")
class Puppy(Dog):
    def func3(self):
        print("This is the child class of Dog")
obj=Puppy()
obj.func1()
obj.func2()
obj.func3()
obj2=Dog()
obj2.func1()
obj2.func2()
obj3=Animal()
obj3.func1()

#multiple inheritance
class A:
    def func(self):
        print("This is the parent class of C")
class B:
    def func(self):
        print("This is also another parent class of C")
class C(A,B):
    def func1(self):
        print("This is the class for C")
obj=C()
obj.func()
obj.func()
obj.func1()
obj1=B()
obj1.func()
obj2=A()
obj2.func()

#hierarchical inheritance
class A:
    pass
class B(A):
    pass
class C(A):
    pass
obj=C()
obj1=B()
obj2=A()

