#
# MIT OCW ODE Mathlet Isoclines replacement in Python
#
from pylab import *
xmax = 4.0
xmin = -xmax
D = 20
ymax = 4.0
ymin = -ymax
x = linspace(xmin, xmax, D)
y = linspace(ymin, ymax, D)
X, Y = meshgrid(x, y)
deg = arctan(Y**2 - X)
QP = quiver(X,Y,cos(deg),sin(deg))
show()
