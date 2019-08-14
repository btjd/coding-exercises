"""
Leetcode 70
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?
"""

def climbing_stairs(n):
    cache = {}
    count = [0]
    def helper(step, n):
        if step in cache:
            return cache[step]
        if step > n:
            return 0
        if step == n:
            return 1
        else:
            cache[step] = helper(step + 1, n) + helper(step + 2, n)
        return cache[step]
    return helper(0, n)

def test_climbing_stairs():
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(5) == 8
    assert climbing_stairs(35) == 14930352