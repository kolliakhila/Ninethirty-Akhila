#Assignment 1
a=int(input("Enter a number:"))
b=int(input("Enter a second number:"))
operator=input("Enter a operator (+,-,*,/):")

def add(a,b):
    print("Result:",a+b)
def subtract(a,b):
    print("Result:",a-b)
def multiple(a,b):
    print("Result:",a*b)
def divide(a,b):
    if b==0:
        print("Cannot divide by zero")
    else:
        print("Result:",a/b)
if operator=="+":
    add(a,b)
elif operator=="-":
    subtract(a,b)
elif operator=="*":
    multiple(a,b)
elif operator=="/":
    divide(a,b)
else:
    print("Invalid choice")

#Assignment 2
number=int(input("Enter a number:"))
def check_even_odd(number):
    if number%2==0:
        print("Even")
    else:
        print("Odd")
num=check_even_odd(number)

#Assignment 3
student_name=input("Enter name :")
student_grade=input("Enter grade:")

def student_info(name,grade):
    print("Name:",student_name)
    print("Grade:",student_grade)

student_info(student_name,student_grade)

#Assignment 4
num=int(input("Enter a number:"))
def generate_table(number):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)
generate_table(num)






