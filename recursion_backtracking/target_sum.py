"""
LeetCode 494
You are given a list of non-negative integers, 
a1, a2, ..., an, and a target, S. Now you have 
2 symbols + and -. For each integer, you should 
choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make 
sum of integers equal to target S.
"""
############################################
# This solution times out for large inputs #
# needs to be improved with memoization or #
# bottom up DP approach                    #
############################################
def target_sum(nums, S):
    count = [0]
    def _helper(nums, i, seq_sum):
        if i == len(nums):
            if seq_sum == S:
                count[0] += 1
        else:
            _helper(nums, i+1, seq_sum + nums[i])
            _helper(nums, i+1, seq_sum - nums[i])
    _helper(nums, 0, 0)
    return count[0]

def test_target_sum():
    target_sum([1, 1, 1, 1, 1], 3) == 5