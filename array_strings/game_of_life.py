def game_of_life(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    
    LeetCode 289. 
    
    The problem asks for an in place solution, this does
    not achieve that, the results are populated in a new matrix that is
    then returned.
    """
    num_rows = len(board)
    num_cols = len(board[0])
    res_board = [[0 for r in range(num_cols)] for c in range(num_rows)]
    def get_live_neighbors(r, c):
        live_neighbors = 0
        row = r
        col = c
        print(row, col)
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if r == row and c == col:
                    continue
                elif 0 <= r < num_rows and 0<= c < num_cols:
                    print(r, c)
                    if board[r][c] == 1:
                        live_neighbors += 1
        return live_neighbors
    for row in range(num_rows):
        for col in range(num_cols):
            ln = get_live_neighbors(row, col)
            print(ln)
            if board[row][col] == 1:
                if ln < 2:
                    res_board[row][col] = 0
                elif ln == 2 or ln == 3:
                    res_board[row][col] = 1
                elif ln > 3:
                    res_board[row][col] = 0
            elif board[row][col] == 0:
                if ln == 3:
                    res_board[row][col] = 1
    return res_board

print(game_of_life([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])) # [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]