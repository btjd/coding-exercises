"""
LeetCode 200
Given a 2d grid map of 1's (land) and 0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are 
all surrounded by water.
"""
def number_of_islands(grid):
    if not grid:
        return None
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0
    # This helper function just labels
    # all the connected land cells as
    # 'v' for visited.
    def _helper(r, c):
        if grid[r][c] == 0 :
            return
        else:
            print(r, c)
            grid[r][c] = 'v'
            if r-1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] = 'v'
                _helper(r-1, c)
            if c+1 < num_cols and grid[r][c+1] == 1:
                grid[r][c+1] = 'v'
                _helper(r, c+1)
            if r+1 < num_rows and grid[r+1][c] == 1:
                grid[r+1][c] = 'v'
                _helper(r+1, c)
            if c-1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] = 'v'
                _helper(r, c-1)
    for r in range(num_rows):
        for c in range(num_cols):
            # Showing both cases for readability,
            # could be a single check. If current
            # cell is 0 or has already been visited, pass
            if grid[r][c] == 'v' or grid[r][c] == 0:
                pass
            else:
                # If we find a cell that has 1,
                # increment island count before 
                # you recursively label all the
                # land cells it touches as visited
                num_islands += 1
                _helper(r, c)
    return num_islands
            
def test_num_islands():
    assert number_of_islands([[1,1,0], [0,1,0], [0,0,0]]) == 1
    assert number_of_islands([[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]) == 3
    assert number_of_islands([[1,1,1], [0,1,0], [1,1,1]]) == 1
    assert number_of_islands([[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]) == 1

