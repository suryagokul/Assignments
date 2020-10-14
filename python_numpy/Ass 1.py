import numpy as np

arr = np.array([1, 2, 3,  4, 5])

N = 4

Mat = [arr**(N-i-1) for i in range(N)]


print(np.column_stack(Mat))

