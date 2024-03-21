import matrix

matrix1 =  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = matrix.add_matrices(matrix1=matrix1,matrix2=matrix2)

for row in result:
  print(row)
