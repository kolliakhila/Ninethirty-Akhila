import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
C=Circle(4)
R=Rectangle(2,8)
print("Area of circle is:",C.area())
print("Area of rectangle is:",R.area())
