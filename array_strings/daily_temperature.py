"""
LeetCode 739 (This implementation is not optimal ... times out)
Given a list of daily temperatures T, 
return a list such that, for each day in the input, 
tells you how many days you would have to wait until 
a warmer temperature. If there is no future day for 
which this is possible, put 0 instead.

This implementation uses a sliding window approach
"""
def daily_temperature(T):
    if not T:
        return []
    start = 0
    end = 1
    result = [0] * len(T)
    while start < len(T)-1:
        if T[end] > T[start]:
            result[start] = end - start
            start += 1
            end = start + 1
        else:
            if T[end] <= T[start] and end == len(T)-1:
                result[start] = 0
                start += 1
                end = start + 1
            else:
                end += 1
    return result

def test_daily_temps():
    assert daily_temperature([73, 74, 75, 71, 69, 72, 76, 73]) == [1 ,  1,  4,  2,  1,  1,  0,  0]
    assert daily_temperature([47, 47, 47, 47, 47, 47, 47, 47]) == [ 0,  0,  0,  0,  0,  0,  0,  0] 
    assert daily_temperature([55,38,53,81,61,93,97,32,43,78]) == [3 , 1, 1, 2, 1, 1, 0, 1, 1, 0]