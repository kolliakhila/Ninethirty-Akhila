def remove_duplicates(list):
    unique=[]
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique
list=[1,3,4,1,4,3,6,7,0]
print(remove_duplicates(list))
