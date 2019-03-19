from collections import deque
"""
LeetCode 733
An image is represented by a 2-D array of integers, each integer representing
 the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) 
of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels 
connected 4-directionally to the starting pixel of the same color as the 
starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color as the starting pixel), and so on. Replace the 
color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""
def flood_fill(image, sr, sc, new_color):
    old_color = image[sr][sc]
    def get_neighbors(r, c):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        neighbors = []
        for d in directions:
            row = r + d[0]
            col = c + d[1]
            if (row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or image[row][col] != old_color or image[row][col] == new_color):
                continue
            else:
                neighbors.append((row, col))
        return neighbors
    # BFS, could also use DFS, or recursion
    q = deque()
    q.append((sr, sc))
    while q:
        current_cell = q.popleft()
        image[current_cell[0]][current_cell[1]] = new_color
        q.extend(get_neighbors(current_cell[0],current_cell[1]))
    return image
    
def test_flood_fill():
    assert flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    assert flood_fill([[0,0,0],[0,1,1]], 1, 1, 1) == [[0,0,0],[0,1,1]]