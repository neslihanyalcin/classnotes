import numpy as np
import scipy.linalg as lin

DB = lin.toeplitz([1, -1, 0], [1, 0, 0])
print "backward"
print DB

DF = lin.toeplitz([-1, 0, 0], [-1, 1, 0])
print "forward"
print DF

print "\n"

print np.dot(DF, DB)
