"""
LeetCode 560
Given an array of integers and an integer k, 
you need to find the total number of continuous 
subarrays whose sum equals to k.
"""
def subarray_sum_linear(nums, k):
    # Approach #4 at: https://leetcode.com/articles/subarray-sum-equals-k/
    count = 0
    csum = 0
    # When csum = k, then the difference is 0
    # See animation in approach#4 of the
    # linked article
    cache = {0:1}
    for i in range(len(nums)):
        csum += nums[i]
        if csum - k in cache:
            count += cache[csum - k]
        if csum not in cache:
            cache[csum] = 1
        else:
            cache[csum] += 1
    return count

def subarray_sum_quadratic(nums, k):
    count = 0
    for start in range(len(nums)):
        csum = 0
        for end in range(start, len(nums)):
            csum += nums[end]
            if csum == k:
                count += 1
    return count

def test_subarray_sum():
    assert subarray_sum([3,7,4,3,7], 7) == 3