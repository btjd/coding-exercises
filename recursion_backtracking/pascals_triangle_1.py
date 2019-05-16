"""
LeetCode 118
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

def generate(num_rows):
    triangle = [[1],[1,1]]
    cache = {}
    for i in range(2, num_rows):
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
    for row in range(2, num_rows):
        for col in range(row + 1):
            triangle[row][col] = helper(row, col)
    return triangle

def test_generate():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]