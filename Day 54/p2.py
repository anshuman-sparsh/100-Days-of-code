import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Addition:\n", A + B)
print("Subtraction:\n", A - B)
print("Matrix Multiplication:\n", np.dot(A, B))  # or A @ B
