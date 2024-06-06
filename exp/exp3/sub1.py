import numpy as np

x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1: ,::2] = -99
print(x)

x.max(axis=1)

rng = np.random.default_rng()
samples = rng.normal(size=2500)
print(samples)

# output:

# [[  0   1   2   3   4]
#  [-99   6 -99   8 -99]
#  [-99  11 -99  13 -99]]
# [-1.45160979 -2.59074424  1.55704938 ...  0.03404351 -1.56502679
#  -0.19073136]