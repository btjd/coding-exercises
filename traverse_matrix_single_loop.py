"""
Write a function that takes in a nested array and 
traverses it using only one loop
"""

def traverse_matrix_single_loop(arr):
    res = []
    for i in range(len(arr)**2):
        res.append(arr[i/len(arr)][i%len(arr)])
    return res


# traverse_matrix_single_loop([[1,2,],[3,4]])
print traverse_matrix_single_loop([[1,2,3,4],[5,6,7,8,],[9,10,11,12],[13,14,15,16]])