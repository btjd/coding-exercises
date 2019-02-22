"""
LeetCode 724
Given an array of integers nums, write a method that returns 
the "pivot" index of this array.

We define the pivot index as the index where the sum of the 
numbers to the left of the index is equal to the sum of the 
numbers to the right of the index.

If no such index exists, we should return -1. If there are 
multiple pivot indexes, you should return the left-most 
pivot index.
"""
def find_pivot_index(nums):
    # if len(nums)  <= 2:
    #     return -1
    # tot_sum = sum(nums)
    # i = 1
    # while i < len(nums) - 1:
    #     if sum(nums[:i]) == tot_sum - sum(nums[:i+1]):
    #         return i
    #     else:
    #         i += 1
    # return -1

    if len(nums)  <= 2:
        return -1
    tot_sum = sum(nums)
    i = 0
    cumul_sum = 0
    while i < len(nums):
        if cumul_sum == tot_sum - (cumul_sum + nums[i]):
            return i
        else:
            cumul_sum += nums[i]
            i += 1
    return -1

def test_find_pivot_index():
    assert find_pivot_index([1, 7, 3, 6, 5, 6]) == 3