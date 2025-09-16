#Rotate a list by k elements
def rotate_list(nums,k):
    n=len(nums)
    if nums==0:
        return nums
    k=k%n
    return nums[-k:]+nums[:-k]
nums=[1,2,3,4,5,6,7,8,9,0]
k=3
print(rotate_list(nums,k))