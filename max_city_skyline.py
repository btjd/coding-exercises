"""
LeetCode 807
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. 
We are allowed to increase the height of any number of buildings, by any amount (the amounts can be 
different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, 
and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour 
of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?
"""

def max_increase_skyline(grid):
    height_sum = 0
    tb_skyline = []
    rl_skyline = []
    n = len(grid)
    
    # Obtain skyline viewed from right or left.
    # i.e, the max values of every row
    for row in grid:
        rl_skyline.append(max(row))
    # Obtain skyline viewed from top or bottom.
    # i.e, the max value of every column
    for col in range(n):
        temp_col = []
        for row in grid:
            temp_col.append(row[col])
        tb_skyline.append(max(temp_col))
    # Finally, the new building height is the min
    # cross section between tb_skyline and rl_skyline
    # then find the difference with the original height
    # and add it to our counter return variable
    for c in range(n):
        for r in range(n):
            height_sum += min(tb_skyline[c], rl_skyline[r]) - grid[c][r]
    return height_sum

def test_max_skyline():
    assert max_increase_skyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]) == 35