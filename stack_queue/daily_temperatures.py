"""
LeetCode 739
Given a list of daily temperatures T, return a list such that, 
for each day in the input, tells you how many days you would 
have to wait until a warmer temperature. If there is no future 
day for which this is possible, put 0 instead.
For example, given the list of temperatures 
T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Algorithm:
Traverse the list backwards and use a stack where every iteration
we check if the top of it has a temp that is higher than the current
in which case we keep poping until we find a lower one (when going
in reverse, it means we keep an order of coldet to hotter). The ans
array for a certain index is the difference of whatever is at the top
of the stack (the next warmer temp) and the index of the current temp.
"""

def daily_temperatures(T):
    ans = [0] * len(T)
    stack = [] #indexes from hottest to coldest
    for i in range(len(T) - 1, -1, -1):
        # We pop temps that are lower than our current
        # temp or until the stack is empty. If we pop til
        # the stack gets empty, it means there were no higher
        # temps for the remainder of T from our current position
        # and so the current value of ans[i] should remain its 
        # default value of 0.
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        # At this point either the current temp is smaller than
        # What's at the top of the stack, in which case we compute
        # the number of days for the current position which is the
        # difference between top of stack (next warmer temp) and the
        # current indes, or, the stack is empty and we just skip,
        # meaning the value of our current ans remains 0 because 
        # we couldn't find a day with a warmer temp.
        if stack:
            ans[i] = stack[-1] - i
        # In either case, we push to the top of the stack the index
        # of the current temp.
        stack.append(i)
    return ans

def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]