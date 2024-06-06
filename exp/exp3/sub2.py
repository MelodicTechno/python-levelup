import numpy as np
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
print(A)
A = linalg.inv(A)
print(A)

# output
# [[  0   1   2   3   4]
#  [-99   6 -99   8 -99]
#  [-99  11 -99  13 -99]]
# [-1.45160979 -2.59074424  1.55704938 ...  0.03404351 -1.56502679
#  -0.19073136]
