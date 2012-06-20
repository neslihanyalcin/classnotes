import scipy.linalg as lin
import numpy as np
from pylab import *

data = np.genfromtxt("synthetic_control.data", dtype=float)

# before norm
data = data[:,0:10]

print data.shape

# show the mean, and std of the first time series
print data[0,:]
print np.mean(data[0,:], axis=0)
print np.std(data[0,:], axis=0)

# normalize
data -= np.mean(data, axis=0)
data /= np.std(data, axis=0)

# after norm
print data[0,:]

u,s,v = lin.svd(data)
print 'svd'
print u.shape
print s
print v.shape

plot(u[:,0], u[:,1], '.')

show()
