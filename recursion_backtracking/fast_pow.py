"""
Leetcode 50
Implement pow(x, n), which calculates x raised to the power n (xn)

Explanation of Algorithm
https://www.youtube.com/watch?v=-3Lt-EwR_Hw
"""

def fast_exponent(x, n):
    def fast_pow(x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        res = fast_pow(x, n/2)
        if n % 2 == 0:
            return res * res
        else:
            return x * res * res
    if n < 0:
        x = 1/x
        n = -n
    return fast_pow(x, n)

def test_fast_exponent():
    assert fast_exponent(2.00000, 10) == 1024
    assert fast_exponent(2.00000, -2) == 0.25