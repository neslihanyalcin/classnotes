import numpy as np
import numpy.linalg as lin

A = np.loadtxt('A_matrix')
AtA = np.dot(A.T,A)
print AtA

print "chol on AtA", lin.cholesky(AtA)

q,r = lin.qr(A)
print "qr on A", r.T

B = np.array([[3, 4, 5, 6],[3, 4, 5, 2],[3, 4, 5, 6],[3, 4, 5, 2]])
print 'AB',         
print np.dot(A,B)

