#finding all prime numbers upto n
def primes_upto_n(n):
    primes=[]
    for num in range(2,n+1):
        is_prime=True
        for i in range(2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
                primes.append(num)
    return primes
print(primes_upto_n(20))    

#Check a prime number
num=int(input("Enter a number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is a prime")
            break
        else:
            print(num,"is not a prime")
else:
    print(num,"is not a prime")