#Exception with ZeroDivisionError
try:
    x=12/2
except ZeroDivisionError:
    print("Error occurred")
else:
    print("Result is:",x)
finally:
    print("This code runs successfully")

#Exceptions with ValueError
try:
    a=int(input("Enter a number:"))
except ValueError:
    print("There is no invalid input")
finally:
    print("Executed successfully")

#Exceptions with Exception
try:
    int("xyz")
except Exception as e:
    print("Caught Exception:", e)

#Exceptions with IndexError
try:
    [1, 2, 3][10]
except IndexError:
    print("IndexError occurred")

#Exceptions with NameError
try:
    print(undefined_variable)
except NameError:
    print("NameError occurred")

#Exceptions with ModuleNotFoundError
try:
    import abcdefg
except ModuleNotFoundError:
    print("ModuleNotFoundError occurred")
