def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

print(transpose([[1, 2], [3, 4]]))  # Example: [[1, 3], [2, 4]]