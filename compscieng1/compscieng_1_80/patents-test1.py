from scipy.signal import *
import numpy as np


a = np.array([  4.,   3.,   2.,   8.,   4.,  
                4.,  10.,   4.,  10.,   7.])
d = 0.15 
res = lfilter((1,),(1,d-1),a) 
k = [a[0]] 
for inv in a[1:]: k.append((1-d)*k[-1] + inv) 
print np.array(k) 
