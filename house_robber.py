"""
Leetcode 198
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money 
of each house, determine the maximum amount of money you can rob 
tonight without alerting the police.

https://www.youtube.com/watch?v=GzaoEn8wF_U
"""

def rob(nums):
    even_sum = 0
    odd_sum = 0
    for i in range(len(nums)):
        if i % 2 ==0:
            even_sum = max(even_sum + nums[i], odd_sum)
        else:
            odd_sum = max(odd_sum + nums[i], even_sum)
    return max(odd_sum, even_sum)

print(rob([1, 50, 3, 4, 55, 1]))