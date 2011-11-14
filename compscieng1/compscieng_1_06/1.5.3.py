import numpy as np
import scipy.linalg as lin
import ktbc

K,T,B,C =  ktbc.ktbc(5)

u,v=lin.eig(K)

print u

print 2-np.sqrt(3), 2-1, 2-0, 2+1, 2+np.sqrt(3)

print 2*np.ones((5,1)).T - 2*np.cos((np.arange(5)+1) * np.pi/6)
