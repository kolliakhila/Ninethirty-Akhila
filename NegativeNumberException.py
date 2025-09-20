class NegativeNumberError(Exception):
    pass
def check_num(num):
    if num<0:
        raise NegativeNumberError("Negative numbers are not allowed")
    else:
        print("Valid number",num)
try:
    n=int(input("enter a num:"))
    check_num(n)
except NegativeNumberError as e:
    print("Error:",e)