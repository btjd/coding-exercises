"""
LeetCode 463
You are given a map in form of a two-dimensional integer grid
where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly 
one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected 
to the water around the island). One cell is a square with side length 1. 
The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
"""
def island_perimeter(grid):
    perimeter = 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r + 1 < num_rows and grid[r+1][c] == 1: 
                    perimeter -= 1
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    perimeter -= 1
                if c + 1 < num_cols and grid[r][c+1] == 1:
                    perimeter -= 1
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    perimeter -= 1
    return perimeter

def test_island_perimeter():
    assert island_perimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16