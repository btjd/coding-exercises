def spiral_traversal(matrix):
    def rotate_counter_clockwise(grid):
        rows = len(grid)
        cols = len(grid[0])
        flattened = []
        rotated = [[0 for i in range(rows)] for j in range(cols)]
        rotated_rows = len(rotated)
        rotated_cols = len(rotated[0])
        for r in range(rows):
            for c in range(cols):
                flattened.append(grid[r][c])
        for c in range(rotated_cols-1, -1, -1):
            for r in range(rotated_rows):
                rotated[r][c] = flattened.pop()
        return rotated
    spiral_sequence = []
    rows = len(matrix)
    cols = len(matrix[0])
    while len(matrix) > 0:
        if len(matrix) == 1:
            spiral_sequence.extend(matrix.pop())
            break
        else:
            spiral_sequence.extend(matrix[0])
            matrix = rotate_counter_clockwise(matrix[1:])
    return spiral_sequence

# someone else's implementation
def spiral_order(matrix):
    answ = []
    while len(matrix) > 1:
    #top
        answ += matrix[0]
        matrix.pop(0)
        
    #right side
        answ += [x[-1] for x in matrix]
        for x in matrix:
            x.pop(-1)
            
    #bottom
        answ += matrix[-1][::-1]
        matrix.pop(-1)

    #left side
        answ += [x[0] for x in matrix][::-1]
        for x in matrix:
            x.pop(0)

    answ += matrix[0]
    return answ

def test_spiral_matrix():
    assert spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]