numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num= [x for x in numbers if x % 2 == 0]
odd_squares = [x**2 for x in numbers if x % 2 != 0]
div_by_3 = [(x, x**2) for x in numbers if x % 3 == 0]

print("Even numbers:", even_num)
print("Squares of odd numbers:", odd_squares)
print("Numbers divisible by 3 with their squares:", div_by_3)
