#sum of multiples of 3 or 5 below 1000
n=1000
sum=0
for i in range(1,n):
    if i%3==0 or i%5==0:
        sum=sum+i
print("sum of all multiples of 3 or 5 is:",sum)


Fibonacci sequence sum of the even valued terms
a,b=0,1
Even_sum=0
while a <=4000000:
    if a%2==0:
        Even_sum=Even_sum+a
    a,b=b,a+b
print("Sum of all even terms in fibonacci sequence below 4000000 is:",Even_sum)

#