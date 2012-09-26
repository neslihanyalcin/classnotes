from pylab import *
import numpy as np

data = loadtxt("dell.csv")

print np.mean(data)

print np.median(data)

print np.std(data)

print np.mean(data)+2*np.std(data)

print np.percentile(data, 95)

#hist(data,100)

#show()
