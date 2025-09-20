#Exceptions with ZeroDivisionError
try:
    numerator=int(input("Enter a number:"))
    denominator=int(input("Enter a number"))
    result=numerator/denominator
    print("Result is:",result)
except ZeroDivisionError:
    print("Division by Zero is not allowed")
finally:
    print("Execution completed")
