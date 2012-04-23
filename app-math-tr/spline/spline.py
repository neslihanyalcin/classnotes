import numpy as np
import scipy.linalg as lin

x = np.array([4.,9.,12.,16.,22.])

y = np.array([157.,41.,145.,92.,7.])

h = np.diff(x)

dy = np.diff(y)

s = dy / h

ds = np.diff(s)

s3 = 3 * ds

a = np.array([[ 2*(h[0]+h[1]), h[1], 0],
              [ h[1], 2*(h[1]+h[2]), h[2]],
              [ 0, h[2], 2*(h[2]+h[3])]])

p,l,u = lin.lu(a)

y = lin.solve(l,s3.T)

x = lin.solve(u,y)

