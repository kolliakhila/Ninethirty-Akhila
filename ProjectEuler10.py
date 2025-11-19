# #sum of multiples of 3 or 5 below 1000
# n=1000
# sum=0
# for i in range(1,n):
#     if i%3==0 or i%5==0:
#         sum=sum+i
# print("sum of all multiples of 3 or 5 is:",sum)


# #Fibonacci sequence sum of the even valued terms
# a,b=0,1
# Even_sum=0
# while a <=4000000:
#     if a%2==0:
#         Even_sum=Even_sum+a
#     a,b=b,a+b
# print("Sum of all even terms in fibonacci sequence below 4000000 is:",Even_sum)

#Find largest prime factor of given number
# def largest_primefactor(n):
#     largest=None
#     while n%2==0:
#         largest=2
#         n=n//2
#     i=3
#     while i*i<=n:
#         while n%i==0:
#             largest=i
#             n=n//i
#         i+=2
#     if n>1:
#         largest=n
#     return largest
# number=600851475143
# print("Largest prime factor of 600851475143 is :",largest_primefactor(number))

#Largest palindrome made from the product of two 3-digit numbers
def is_palindrome(n):
    s=str(n)
    return s==s[::-1]
max_palin=0
factors=(0,0)

for a in range(100,1000):
    for b in range(a,1000):
        p=a*b
        if p>max_palin and is_palindrome(p):
            max_palin=p
            factors=(a,b)
print("Largest palindrome made from the product of two 3-digit numbers is:",max_palin)
print("factors are:",factors)

#smallest positive number that is evenly divisible by all of the numbers from 1 to 20
