import copy
original_list= [[1, 2, 3], [4, 5, 6]]
print("Original:", original_list)

shallow_copy = copy.copy(original_list)

deep_copy = copy.deepcopy(original_list)

original_list[0][0] = 99   

print("\nAfter modification:")
print("Original:", original_list)
print("Shallow copy:", shallow_copy)
print("Deep copy:", deep_copy)
