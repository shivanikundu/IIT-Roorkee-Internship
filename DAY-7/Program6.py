#NumPy : matrix multiplication without loops
import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
C = np.matmul(A, B)

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nResult of A × B:")
print(C)