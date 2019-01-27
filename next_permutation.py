"""
LeetCode 31
Implement next permutation, which rearranges numbers 
into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as 
the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Algorithm:
If we take as an example, the array [1, 2, 3, 6, 5, 4]
1) Starting at the right end side (4), and traversing to 
   the left end side, find the first smaller element:
   4 -> 5 -> -> 6 -> "3", "3" is the anchor 'a'
2) Sort the subarray to the right of the anchor:
   [1,2,"3",6,5,4] -> [1,2,"3",4,5,6]
3) Finally, find the next greater element in the
   [4,5,6] subarray and swap it with the anchor element.
   Note: It's not alway going to be the first element of 
   the subarray (4 in this example).
References:
   - https://youtu.be/quAS1iydq7U?t=467
   - https://youtu.be/hPd4MFdg8VU?t=180
   - https://youtu.be/zGQq3HGBTXg?t=123
"""
def next_permutation(nums):
    # a is for anchor. Scanning, nums right to left, it's the index 
    # of the first smaller value.
    # e is for end and s is for start, as in the start of the subarray
    # right to the right of a.
    a = len(nums) - 2
    while nums[a] >= nums[a+1] and a >= 0:
        a -= 1
    if a < 0:
        nums.reverse()
    else:
        s = a + 1
        e = len(nums) - 1
        # First reverse the subarray to the right of a
        while s <= e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        # Then look for and swap the element located
        # at a with its first greater value
        for i in range(a+1, len(nums)):
            if nums[i] > nums[a]:
                nums[a], nums[i] = nums[i], nums[a]
                break
    return nums


def test_next_permutation():
    assert next_permutation([1, 2, 3, 6, 5, 4]) == [1, 2, 4, 3, 5, 6]
    assert next_permutation([1, 2, 3]) == [1, 3, 2]
    assert next_permutation([3, 2, 1]) == [1, 2, 3]
    assert next_permutation([1, 3, 2]) == [2, 1, 3]
    assert next_permutation([1, 1, 5]) == [1, 5, 1]
    assert next_permutation([2, 3, 1]) == [3, 1, 2]
    assert next_permutation([5, 1, 1]) == [1 ,1 ,5]