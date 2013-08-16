import numpy as np
import scipy.linalg as lin
import ktbc

K,T,B,C = ktbc.ktbc(4); print K

C = lin.toeplitz([0, -1, 0, 0], [0, 1, 0, 0]); print C

print "ortalanmis",  lin.solve((25*K + 2.5*C), [1.,1.,1.,1.])

F = lin.toeplitz([-1, 0, 0, 0], [-1, 1, 0, 0]); print F

print "ileri farklilik", lin.solve((25*K + 2.5*F), [1.,1.,1.,1.])

def ux(x): return x - 1/(1-np.e) + np.e**x/(1-np.e)

print ux(0.2), ux(0.4), ux(0.6), ux(0.8)

