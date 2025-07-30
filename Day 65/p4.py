import numpy as np

arr = np.array([3.0, 7.0, 10.0, 5.0])

min_val = arr.min()
max_val = arr.max()

normalized = (arr - min_val) / (max_val - min_val)

print("Normalized array:", normalized)
