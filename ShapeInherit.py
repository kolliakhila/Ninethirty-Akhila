class Shape:
    def __init__(self):
        pass
class Circle(Shape):
    def area(self,r):
        self.r=r
        area=3.14*r*r
        print("Area of circle is ",area)
class Rectangle(Shape):
    def area(self,l,b):
        self.l=l
        self.b=b
        area=l*b
        print("Area of rectangle is",area)
A=Shape()
B=Circle()
B.area(5)
C=Rectangle()
C.area(4,6)

# def rev_list(lst):
#     left=0
#     right=len(lst)-1
#     while left<right:
#         temp=lst[left]
#         lst[left]=lst[right]
#         lst[right]=temp
#         left+=1
#         right-=1
#     return lst
# print(rev_list([1,2,3]))
