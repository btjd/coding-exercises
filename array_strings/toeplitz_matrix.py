"""
LeetCode 766
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
"""

def toeplitz(matrix):
    nr = len(matrix)
    nc = len(matrix[0])

    for r in range(nr - 1):
        c = 0
        curr = matrix[r][c]
        r += 1
        c += 1
        while r <= nr -1 and c <= nc - 1:
            if matrix[r][c] == curr:
                r += 1
                c += 1
            else:
                return False

    for c in range(1, nc - 1):
        r = 0
        curr = matrix[r][c]
        r += 1
        c += 1
        while r <= nr -1 and c <= nc - 1:
            if matrix[r][c] == curr:
                r += 1
                c += 1
            else:
                return False

    return True

def test_toeplitz():
    assert toeplitz([[1,2,3,4],[5,1,2,3],[9,5,1,2]]) is True
    assert toeplitz([[1,2],[2,2]]) is False
    assert toeplitz([[1,2,3],[5,1,2],[4,5,2]]) is False