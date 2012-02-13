import numpy as np
import scipy.linalg as lin

#np.linalg.lstsq(B,b)

A = np.array([[6.,1.,1.],
              [1.,7.,1.],
              [1.,1.,8.]])
b = [1.,1.,1.]
print A

xreal = lin.solve(A, b); print "solution", xreal

P = np.diag(np.diag(A)); print "P",P
x = np.zeros(A.shape[0]); print x
J = lin.solve(P,P-A)
c = lin.solve(P,b)
print "J",J
print "c",c
for i in range(10):
    x = np.dot(J,x) + c
    print x
