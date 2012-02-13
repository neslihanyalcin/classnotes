import numpy as np
import numpy.linalg as lin

A = np.array([[3., 4.],[5., 6.]])
m,n = A.shape
R = np.zeros((m,n))
Q = np.zeros((m,n))

for j in range(n):
    v = A[:,j]
    for i in range(j):
        R[i,j] = np.dot(Q[:,i].T,A[:,j])
        v=v-np.dot(R[i,j],Q[:,i])
    R[j,j] = lin.norm(v)
    Q[:,j] = v/R[j,j]

