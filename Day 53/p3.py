import numpy as np

arr = np.arange(1, 13).reshape(3, 4)

print("Full Array:\n", arr)
print("Second row:", arr[1])
print("Last column:", arr[:, -1])
