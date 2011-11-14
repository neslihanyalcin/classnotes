import numpy as np
import scipy.linalg as lin

A = np.array([[2,3],[4,5]])
B = np.array([[1,2],[2,4]])

print np.dot(A,B)

# rows of A times columns of B, i=0, j=0
print np.dot(A[0,:].reshape((1,2)),
             B[:,0].reshape((2,1)))

# columns of A times rows of B
print np.dot(A[:,0].reshape((2,1)),B[0,:].reshape((1,2))) + \
    np.dot(A[:,1].reshape((2,1)),B[1,:].reshape((1,2)))

