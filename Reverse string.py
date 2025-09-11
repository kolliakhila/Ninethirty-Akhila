#using join reversed method
def reverse_string(str):
    return "".join(reversed(str))
print(reverse_string("python"))

#using loop
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev   
    return rev

print(reverse_string("hello"))  


