import numpy as np

arr = np.arange(1, 11)
squared = arr ** 2
print("Squared Array:", squared)

filtered = squared[squared > 25]
print("Filtered (>25):", filtered)
