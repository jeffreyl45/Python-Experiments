# recursively computes the sum of a list
def sum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum(nums[1:])
print(sum([1,2,3,4]))