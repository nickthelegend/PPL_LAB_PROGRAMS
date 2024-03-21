def add_matrices(matrix1, matrix2):
  # Ensure both matrices have the same dimensions
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
      raise ValueError("Matrices must have the same dimensions")
  
  # Initialize a result matrix
  result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  
  # Iterate through rows and columns to add corresponding elements
  for i in range(len(matrix1)):
      for j in range(len(matrix1[0])):
          result[i][j] = matrix1[i][j] + matrix2[i][j]
  
  return result
