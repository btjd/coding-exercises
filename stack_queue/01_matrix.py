"""
LeetCode 542
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Algorithm:
The naive solution is to find every cell containinga 1, then do a BFS until a 0 is found.
The path can be looked at in a reverse manner where we start from every zero that we first
push to a queue and also pre-populate every cell containing 1 with a very large number. 
For every iteration of BFS, we increment the current cell value z by 1. If it's a 0 it becomes
1 and if one of the neighbors value is greater, then it's inf or a greater pre-computed 
distance in which case we need to update it with the current z.
"""

from collections import deque

def update_matrix(matrix):
    q = deque()
    num_rows, num_cols = len(matrix), len(matrix[0])
    for row in xrange(num_rows):
        for col in xrange(num_cols):
            if matrix[row][col] != 0:
                matrix[row][col] = float('inf')
            else:
                q.append((row, col))
    while q:
        i, j = q.popleft()
        for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
            z = matrix[i][j] + 1
            if 0 <= r < num_rows and 0 <= c < num_cols and matrix[r][c] > z:
                matrix[r][c] = z
                q.append((r, c))
    return matrix

def test_update_matrix():
    assert update_matrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]