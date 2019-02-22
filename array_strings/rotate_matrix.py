def rotate(arr, n):
    flattened = []
    rotated = [[0 for i in range(n)] for j in range(n)]
    for r in range(n):
        for c in range(n):
            flattened.append(arr[r][c])
    print(flattened)
    for c in range(n):
        for r in range(n-1, -1, -1):
            print(r, c)
            rotated[r][c] = flattened.pop()
    return rotated

print(rotate([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]], 3))