"""
Implement a function that assigns correct numbers in a field of
Minesweeper, which is represented as a 2 dimensional array.
Example: The size of the field is 3x4, and there are bombs at the positions
[0,0] (row index = 0, column index = 0) and [0,1] (row index = 0, column index = 1).
Then, the resulting field should be:
[[-1, -1, 1, 0]
 [2, 2, 1, 0],
 [0, 0, 0, 0]]
 Your function should return the resulting 2D array after taking the
 following three arguments:
 1) bombs: A list of bomb locations.
 2) num_rows: The number of rows in the resulting field.
 3) num_cols: The numver of columns in the resulting field.
"""

# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    def get_neighbors(cell, num_rows, num_cols):
        neighbors = set()
        if cell[0] > 0:
            if cell[1] > 0:
                neighbors.add((cell[0]-1, cell[1]-1))
                neighbors.add((cell[0]-1, cell[1]))
                neighbors.add((cell[0], cell[1]-1))
            if cell[1] < num_cols-1:
                neighbors.add((cell[0]-1, cell[1]))
                neighbors.add((cell[0]-1, cell[1]+1))
                neighbors.add((cell[0], cell[1]+1))
            else:
                neighbors.add((cell[0]-1, cell[1]))
        if cell[0] < num_rows-1:
            if cell[1] > 0:
                neighbors.add((cell[0], cell[1]-1))
                neighbors.add((cell[0]+1, cell[1]-1))
                neighbors.add((cell[0]+1, cell[1]))
            if cell[1] < num_cols-1:
                neighbors.add((cell[0]+1, cell[1]))
                neighbors.add((cell[0]+1, cell[1]+1))
                neighbors.add((cell[0], cell[1]+1))
            else:
                neighbors.add((cell[0]+1, cell[1]))
        return neighbors
                
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for bomb in bombs:
        field[bomb[0]][bomb[1]] = -1
    for r in range(num_rows):
        for c in range(num_cols):
            bomb_count = 0
            if field[r][c] == -1:
                continue
            else:
                neighs = get_neighbors([r,c], num_rows, num_cols)
                for s in neighs:
                    if field[s[0]][s[1]] == -1:
                        bomb_count += 1
            field[r][c] = bomb_count
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]