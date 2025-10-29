def sum_digits(num):
    sum=0
    while num>0:
        i= num%10
        sum+=i
        num=num//10
    return sum
print(sum_digits(890))