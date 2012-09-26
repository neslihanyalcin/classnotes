from pylab import *
import numpy as np

data = loadtxt("dell.csv")

np.mean(data)

np.median(data)

np.std(data)

np.mean(data)+2*np.std(data)

np.percentile(data, 95)

#hist(data,100)

#show()
