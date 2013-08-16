# this code is converted from Strang's Octave code, 
# not working for every example

import numpy as np
import numpy.linalg as lin

def simplex(A,b,c,basis):
    B=A[:,basis]
    xx,resid,rank,s = lin.lstsq(B,b)
    x = np.zeros(c.shape[0])    
    v = np.zeros(c.shape[0])
    x[basis[0]] = xx[0,0]
    cost = c[basis].T*x[basis]     # cost at starting corner
    for iteration in np.arange(100):
        y = lin.lstsq(B.T,c[basis])           # this y may not be feasible
        y = np.array([y[0]]).T
        idx = (c - np.dot(A.T,y).T).argmin()
        rmin = (c - np.dot(A.T,y).T).min()
        if rmin >= -0.00000001:      # optimality is reached, r>=0
            break                 # current x and y are optimal
         
        print B
        print A 
        print A[:,idx]
        print idx
        v[basis] = lin.lstsq(B,A[:,idx])[0]
        tmp = x[basis] / np.max(v[basis],.000001)
        out = tmp.argmin()
        minratio = tmp.min()
        if v[out] == .000001:  # out = index of first x to reach 0
            break      # break when that edge is extremely short
            
        cost = cost + minratio*rmin  # lower cost at end of step
        x[basis] = x[basis] - minratio*v[basis]   # update old x
        x[idx] = minratio      # find new positive component of x
        basis[out] = idx      # replace old index by new in basis
        print basis
    
    return x,y,cost

if __name__ == '__main__':

    A = np.array([[1, 1, 2], [1, 1, 4]]);
    b = np.array([[4],[4]]);
    basis = np.array([2]);
    c = np.array([5, 1, 8]);
    x,y,cost = simplex(A,b,c,basis)
    print x
    print y
    print cost

    A = np.array([[1, 1, 2]]);
    b = np.array([[4]]);
    basis = np.array([2]);
    c = np.array([5, 3, 8]);
    x,y,cost = simplex(A,b,c,basis)
    print x
    print y
    print cost

