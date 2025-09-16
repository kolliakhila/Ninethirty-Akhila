#Finding second largest number in a list
def second_largest(nums):
    nums=list(set(nums))
    if len(nums)<2:
        return None
    nums.sort()
    return nums[-2]
nums=[25,42,89,19,10,12]
print(second_largest(nums))