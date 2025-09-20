try:
    numerator=int(input("Enter a num for numerator:"))
    denominator=int(input("Enter a num for denominator:"))
    result=numerator/denominator
    print("Result=",result)
except ZeroDivisionError:
    print("Division is not occurred by zero")
except ValueError:
    print("Invalid input")
except Exception as e:
    print("Caught Error:",e)
else:
    print("There is no error in code")
finally:
    print("code executed successfully")