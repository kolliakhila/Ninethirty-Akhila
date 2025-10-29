#using for loop
nested_list = [[1, 2], [3, 4]]
flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(flat_list)

#using list comprehension
nested_list = [[1, 2], [3, 4]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

