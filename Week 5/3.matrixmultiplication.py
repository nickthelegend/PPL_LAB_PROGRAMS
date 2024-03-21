# Multiplication of two matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows of matrix1
for i in range(len(matrix1)):
    # iterate through columns of matrix2
    for j in range(len(matrix2[0])):
        # iterate through rows of matrix2
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# display the result
for row in result:
    print(row)