import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

row_sums = np.sum(arr, axis=1)

print("Row-wise sums:", row_sums)
