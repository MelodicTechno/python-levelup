from math import sin, cos
from scipy import optimize

def f(x):
    x0, x1, x2 = x.tolist()
    return [
        5 * x1 + 3,
        4 * x0 * x0 - 2 * sin(x1 * x2),
        x1 * x2 - 1.5 
    ]

result = optimize.fsolve(f, [1, 1, 1])
print(result)
print(f(result))

# output

# [-0.70622057 -0.6        -2.5       ]
# [0.0, -9.126033262418787e-14, 5.329070518200751e-15]
