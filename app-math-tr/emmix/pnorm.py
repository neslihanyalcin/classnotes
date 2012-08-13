import numpy as np

def pnorm(x, m, s):
    """ 
    Compute the multivariate normal distribution with values vector x,
    mean vector m, sigma (variances/covariances) matrix s
    """
    xmt = np.matrix(x-m).transpose()
    for i in xrange(len(s)):
        if s[i,i] <= sys.float_info[3]: # min float
            s[i,i] = sys.float_info[3]
    sinv = np.linalg.inv(s)
    xm = np.matrix(x-m)
    return (2.0*math.pi)**(-len(x)/2.0)*(1.0/math.sqrt(np.linalg.det(s)))\
            *math.exp(-0.5*(xm*sinv*xmt))

