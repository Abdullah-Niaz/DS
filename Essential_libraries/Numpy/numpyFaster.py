import numpy as np
import time

# Using Python List
lst = list(range(1000000))
start = time.time()
sum_lst = [x * 2 for x in lst]
print("Python List Time:", time.time() - start)

# Using NumPy Array
arr = np.arange(1000000)
start = time.time()
sum_arr = arr * 2  # Vectorized operation
print("NumPy Array Time:", time.time() - start)
