"""
LeetCode 240
"""
def search_matrix(matrix, target):
    def binary_search(sequence, item):
        start = 0
        end = len(sequence)-1
        while start <= end:
            mid = (start + end)//2
            if sequence[mid] == item:
                return True
            else:
                if item < sequence[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return False
    if not matrix:
        return False
    if matrix == [[]] or matrix == []:
        return False
    else:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        for row in matrix:
            if row[0] <= target:
                if binary_search(row, target):
                    return True
        for c in range(num_cols):
            col = [x[c] for x in matrix]
            if col[0] <= target:
                if binary_search(col, target):
                    return True
    return False

def test_search_matrix():
    assert search_matrix([[5],[6]],6) is True
    assert search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20) is False
    assert search_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5) is True