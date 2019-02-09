"""
LeetCode 228
Given a sorted integer array without duplicates, return the summary of its ranges.
"""

def summary_ranges(nums):
    ans = []
    rs = 0
    while rs < len(nums):
        re = rs + 1
        while re < len(nums) and nums[re] == nums[re - 1] + 1:
            re += 1
        if nums[re - 1] == nums[rs]:
            ans.append(str(nums[rs]))
        else:
            ans.append(str(nums[rs]) + "->" + str(nums[re - 1]))
        rs = re
    return ans

def test_summary_ranges():
    assert summary_ranges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
    assert summary_ranges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]