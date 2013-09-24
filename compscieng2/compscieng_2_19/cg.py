import numpy as np
import scipy.linalg as lin

A = np.array([[6.,1.,1.],
              [1.,7.,1.],
              [1.,1.,8.]])

b = np.array([1.,1.,1.])

xreal = lin.solve(A, b); print "solution", xreal

p = b
r = b
x = b*0;
r2 = np.dot(r.T,r)
for i in range(5):
    Ap = np.dot(A,p)
    alpha = r2 / np.dot(p.T,Ap)
    x = x + np.dot(alpha,p)
    r = r-np.dot(alpha,Ap)
    r2old = r2
    r2 = np.dot(r.T,r)
    beta = r2 / r2old
    p = r + np.dot(beta,p)
    print x

       
    
    

