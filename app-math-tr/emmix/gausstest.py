import gauss
import numpy as np
import matplotlib.pyplot as plt

#res = expectation_maximization(np.array([[2,3],[3,4],[5,0],[4,2],[7,2],[5,5] ] ))

data = np.loadtxt('biometric_data_simple.txt',delimiter=',')
data = data[:,1:3]
res = gauss.expectation_maximization(data)
print res
