import numpy as np
import scipy.linalg as lin
T = lin.toeplitz([2, -1, 0])
T[0,0] = 1
J = np.fliplr(np.eye(3))
print T
print np.dot(T,J)
print np.dot(J, np.dot(T,J))

