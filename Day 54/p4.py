import numpy as np

arr = np.arange(1, 13).reshape(3, 4)

print("2nd row:", arr[1])
print("Last column:", arr[:, -1])
print("2x2 center submatrix:\n", arr[0:2, 1:3])
