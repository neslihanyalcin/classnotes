# plotting ax + by + cz = 0, or (ax + by)/-c  = z 
# ax + by + cz = 0 formulu grafikliyoruz ya da, (ax + by)/-c  = z 

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab as p

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-10, 10, 0.5)
Y = np.arange(-10, 10, 0.5)
X, Y = np.meshgrid(X, Y)

Z = (X + 2*Y ) / -3
surf = ax.plot_surface(X, Y, Z,rstride=1, cstride=1, alpha=0.3)

ax.set_zlim3d(0, 30)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
