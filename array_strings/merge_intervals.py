"""
LeetCode 56

Note: This is a slow solution. Evry pop at the first
index, we have to shift the entire array. Might be worth
trying appending merged intervals to a new results
array, trick being, every time we merge, we have to pop
the outdated merged interval from the results array and
update with the latest one. That would not need to be 
done in case there is no merge (lines 30/31)

-Problem statement:
Given a collection of intervals, merge all overlapping intervals.

"""
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if not intervals:
        return []
    intervals.sort()
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= intervals[i-1][1]:
            if intervals[i][1] >= intervals[i-1][1]:
                intervals[i][0] = intervals[i-1][0]
                intervals.pop(i-1)
            elif intervals[i][1] <= intervals[i-1][1]:
                intervals[i] = intervals[i-1]
                intervals.pop(i-1)
        else:
            i += 1
    return intervals

def test_merge():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]