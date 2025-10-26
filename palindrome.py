#using while loop
def is_palindrome(str):
    left=0
    right=len(str)-1
    while left<right:
        if str[left]!=str[right]:
            return False
        left+=1
        right-=1
    return True 
print(is_palindrome("racecar"))

#using for loop
def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):   # loop runs only half the string
        if s[i] != s[n - i - 1]:
            return False
    return True

print(is_palindrome("racecar"))
