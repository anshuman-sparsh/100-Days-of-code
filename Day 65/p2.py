import numpy as np
arr = np.arange(10)

result = np.where(arr > 5, 1, 0)


print("Original:", arr)
print("Modified:", result)