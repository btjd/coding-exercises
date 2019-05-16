"""
LeetCode 119
Given a non-negative index k where k <= 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
"""

def get_row(row_index):
    if row_index == 0:
        return [1]
    elif row_index == 1:
        return [1,1]
    else:
        triangle = [[1],[1,1]]
        cache = {}
        for i in range(2, row_index + 1):
            triangle.append([0] * (i+1))
        def helper(r, c):
            if c == r or c == 0:
                return 1
            else:
                if (r, c) in cache:
                    return cache[(r, c)]
                else:
                    cache[(r, c)] = helper(r - 1, c - 1) + helper(r - 1, c)
                return cache[(r, c)]
        for row in range(2, row_index + 1):
            for col in range(row + 1):
                triangle[row][col] = helper(row, col)
    return triangle [-1]

def test_get_row():
    assert get_row(3) == [1,3,3,1]