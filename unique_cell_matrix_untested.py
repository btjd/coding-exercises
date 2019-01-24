"""
Example given (X is black, O is white): 
Cell is unique when there is no other 
cell containing x in the same row or column
XOOO
OXOO [[x,o,o,o], [o,x,o,o], [o,o,x,x]]
OOXX
The function should return something like ((0,0),(1,1)).
SEE: https://www.geeksforgeeks.org/unique-cells-binary-matrix/
"""
def unique_black(matrix):
    if matrix == []:
        return None    
    num_rows = len(matrix) # 3
    num_cols = len(matrix[0]) # 4
    results = []
    def check_neighbors(cell):
        r = cell[0] #1
        c = cell[1] # 1
        current_row = matrix[r]
        for e in (current_row[:r]+current_row[r+1:]):
            if e == x:
                return False
       for row in matrix - current_row:
           if row[c] == x:
               return False
       return True
    for r in range(num_rows):
        for c in range(num_cols):
            if matrix[r][c] == x and check_neighbors([r,c]):
                results.append([r,c])
                break
   return results
