# recursively finds the largest number in a list
def largestNum(nums):
    if len(nums) == 1:
        return nums[0]
    if nums[0] <= nums[1]:
        nums.remove(nums[0])
    else:
        nums.remove(nums[1])
    return largestNum(nums)
print(largestNum([3,2,4,5,1]))

# recursively finds the smallest number in a list
def smallestNum(nums):
    if len(nums) == 1:
        return nums[0]
    if nums[0] >= nums[1]:
        nums.remove(nums[0])
    else:
        nums.remove(nums[1])
    return smallestNum(nums)
print(smallestNum([3,2,4,5,1]))

