import numpy as np
import scipy.linalg as lin

T = lin.toeplitz([2, -1, 0])

T[0,0] = 1

U = np.array([[1, -1, 0],
              [0, 1, -1],
              [0, 0, 1]])

print np.dot(U.T,U)
print np.dot(U,lin.inv(U))
print np.dot(lin.inv(U), lin.inv(U).T)

