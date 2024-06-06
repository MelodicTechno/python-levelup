import numpy as np

A = np.array([[1, -0.3], [-0.1, 0.9]])
B = np.array([[1, 0.5], [0.7, -0.9]])
evalues, evectors = np.linalg.eig(A)

print(evalues)
print(evectors)

# [[ 0.91724574  0.79325185]
#  [-0.3983218   0.60889368]]
