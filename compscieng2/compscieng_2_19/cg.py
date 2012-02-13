import numpy as np
import scipy.linalg as lin

A = np.array([[6.,1.,1.],
              [1.,7.,1.],
              [1.,1.,8.]])

b = np.array([1.,1.,1.])

xreal = lin.solve(A, b); print "solution", xreal

d = b
r = b
x = b*0;
r2 = np.dot(r.T,r)
for i in range(10):
    Ad = np.dot(A,d)
    alpha = r2 / np.dot(d.T,Ad)
    x = x + np.dot(alpha,d)
    r = r-np.dot(alpha,Ad)
    r2old = r2
    r2 = np.dot(r.T,r)
    beta = r2 / r2old
    d = r + np.dot(beta,d)
    print x

       
    
    

