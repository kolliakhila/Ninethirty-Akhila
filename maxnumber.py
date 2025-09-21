def max_num(nums):
    max_value=nums[0]
    for num in nums[1:]:
        num>max_value
    max_value=num
    return max_value
nums=[10,23,46,5,89]
print(max_num(nums))