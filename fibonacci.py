#fibonacci series upto n terms using recursion
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(8))


#fibonacci series
def fibonacci(n):
    a,b=0,1
    if n<=0:
        print("Invalid input")
    elif n==1:
        print(a)
    else:
        print(a,b,end="")
        for _ in range(2,n):
            c=a+b
            print(c,end="")
            a,b=b,c
fibonacci(9)