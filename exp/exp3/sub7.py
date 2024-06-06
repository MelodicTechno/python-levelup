import numpy as np
import scipy as sp

A = np.array([[1, -0.3], [-0.1, 0.9]])
B = np.array([[1, 0.5], [0.7, -0.9]])
evalues, evectors = sp.linalg.eig(A, B)

print(evalues)
print(evectors)

# [ 0.7367235+0.j -0.9447235+0.j]
# [[-0.93041671  0.08828439]
#  [-0.36650341 -0.99609531]]
