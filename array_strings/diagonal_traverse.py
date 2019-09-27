"""
Leetcode 498
Given a matrix of M x N elements (M rows, N columns), 
return all elements of the matrix in diagonal order 
as shown in the below image.
"""

class Solution:
    
    def find_diagonal_order(self, matrix):
        self.res = []
        if len(matrix) > 0:
            self.nr = len(matrix)
            self.nc = len(matrix[0])
            def dl(current):
                while current[0] < self.nr-1 and current[1] > 0:
                    current[0] += 1
                    current[1] -= 1
                    self.res.append(matrix[current[0]][current[1]])
            def ur(current):
                while current[0] > 0 and current[1] < self.nc-1:
                    current[0] -= 1
                    current[1] += 1
                    self.res.append(matrix[current[0]][current[1]])

            current = [0,0]
            self.res.append(matrix[0][0])
            while current != [self.nr-1, self.nc-1]:
                if current[0] == 0 or current[1] == self.nc-1:
                    if current[1] == self.nc-1:
                        current[0] += 1
                        self.res.append(matrix[current[0]][current[1]])
                        dl(current)
                    else:
                        current[1] += 1
                        self.res.append(matrix[current[0]][current[1]])
                        dl(current)
                else:
                    if current[0] == self.nr-1:
                        current[1] += 1
                        self.res.append(matrix[current[0]][current[1]])
                        ur(current)
                    else:
                        current[0] += 1
                        self.res.append(matrix[current[0]][current[1]])
                        ur(current)
        return self.res

def test_find_diagonal_order():
    obj = Solution()
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    assert obj.find_diagonal_order(m1) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    m2 = [[1,2],[3,4]]
    assert obj.find_diagonal_order(m2) == [1, 2, 3, 4]
    assert obj.find_diagonal_order([]) == []