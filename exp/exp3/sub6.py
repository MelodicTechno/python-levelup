import pylab as pl
import numpy as np
from scipy import linalg

A = np.array([[1, -0.3], [-0.1, 0.9]])
evalues, evectors = linalg.eig(A)

points = np.array([[0, 1.0], [1.0, 0], [1, 1]])

def draw_arrows(points, **kw):
    props = dict(color='blue', arrowstyle='->')
    props.update(kw)
    for x, y in points:
        pl.annotate('',
            xy = (x, y), xycoords='data',
            xytext=(0, 0), textcoords='data',
            arrowprops=props)

draw_arrows(points)
draw_arrows(np.dot(A, points.T).T, color='red')
draw_arrows(evectors.T, alpha=0.7, linewidth=2)
draw_arrows(np.dot(A, evectors).T, color='red', alpha=0.7, linewidth=2)

ax = pl.gca()
ax.set_aspect('equal')
ax.set_xlim(-0.5, 1.1)
ax.set_ylim(-0.5, 1.1)
