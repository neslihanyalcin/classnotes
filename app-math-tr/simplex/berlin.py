import numpy as np
import lp

A = np.array([[1., 1.],[16., 8.],[9000., 5000.]])
b = np.array([44., 512., 300000.])
c = np.array([30000., 20000.])
optx,zmin,is_bounded,sol,basis = lp.lp(c,A,b)
print zmin
print optx
