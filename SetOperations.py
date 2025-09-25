#Returns lists union,intersection and difference using set operations
def set_operations(list1,list2):
    set1,set2 = set(list1),set(list2)
    Union = list(set1|set2)
    Intersection = list(set1&set2)
    Difference = list(set1-set2)
    return Union,Intersection,Difference

lst1=[1,5,7,8]
lst2=[2,5,8,9]

U,I,D=set_operations(lst1,lst2)
print("Union:",U)
print("Intersection:",I)
print("Difference:",D)