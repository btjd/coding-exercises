"""
LeetCode 286
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to 
represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to 
reach a gate, it should be filled with INF.
"""
from collections import deque

def walls_gates(rooms):
    INF = 2147483647
    directions = set([(0,1), (0,-1), (1,0), (-1,0)])
    num_rows = len(rooms)
    if num_rows == 0:
        return
    num_cols = len(rooms[0])
    q = deque()
    for r in range(num_rows):
        for c in range(num_cols):
            if rooms[r][c] == 0:
                q.append((r,c))
    while q:
        current_cell = q.popleft()
        row, col = current_cell
        for move in directions:
            r = row + move[0]
            c = col + move[1]
            if (r < 0 or c < 0 or r >= num_rows or c >= num_cols or rooms[r][c] != INF):
                continue
            else:
                rooms[r][c] = rooms[row][col] + 1
                q.append((r,c))

def test_walls_gates():
    matrix = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    walls_gates(matrix)
    assert matrix == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]