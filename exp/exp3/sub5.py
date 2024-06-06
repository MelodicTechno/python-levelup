"""
最小二乘拟合
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

plt.rcParams[u'font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

X = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Y = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])

def residuals(p):
    k, b = p
    return Y - (k * X + b)

r = optimize.leastsq(residuals, [1, 0])
k, b = r[0]
print("k = ", k, "b = ", b)

# output

# k =  0.6134953491930442 b =  1.794092543259387

def func(x, p):
    A, k, theta = p
    return A*np.sin(2 * np.pi*k*x+theta)

def residuals(p, y, x):
    return y - func(x, p)

x = np.linspace(0, 2*np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6
y0 = func(x, [A, k, theta])

np.random.seed(0)
y1 = y0 + 2 * np.random.randn(len(x))

p0 = [7, 0.40, 0]

plsq = optimize.leastsq(residuals, p0, args=(y1, x))

print(u'真实参数:', [A, k, theta])
print(u'拟合参数:', plsq[0])

plt.plot(x, y1, 'o', label=u"带噪声的实验数据")
plt.plot(x, y0, label=u'真实数据')
plt.plot(x, func(x, plsq[0]), label=u'拟合参数')
plt.legend(loc='best')
plt.savefig(r'exp/exp3/sub5.jpg')
plt.show()
