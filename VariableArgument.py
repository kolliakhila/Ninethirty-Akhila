#Variable positional argument - *args
def multiply(*args):
    result=1
    for i in args:
        result*=i
    return result
print(multiply(3,4))
print(multiply(1,0,3))
print(multiply(5,7,9,8))

#Variable keyword argument - *kwargs
def introduce(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
introduce(name="Akhila",age=21,city="Hyderabad")