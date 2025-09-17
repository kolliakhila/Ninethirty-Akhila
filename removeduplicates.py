def unique_list(lst):
    new_list=[]
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(unique_list([1,1,2,2]))