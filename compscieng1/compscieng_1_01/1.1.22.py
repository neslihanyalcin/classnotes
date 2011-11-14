import scipy.sparse as sparse
import scipy.sparse.linalg
import numpy as np
import scipy.linalg as lin
import matplotlib.pyplot as plt

n = 1000
vec = np.zeros((1,n))
vec[0,0] = 2; vec[0,1] = -1
K = lin.toeplitz(vec)
A = sparse.csc_matrix(K)
e = np.ones((n,1))

u = sparse.linalg.spsolve(A,e)
plt.plot(u)
plt.show()

