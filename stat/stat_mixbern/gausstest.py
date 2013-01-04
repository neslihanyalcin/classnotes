import gauss
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('biometric_data_simple.txt',delimiter=',')
data = data[:,1:3]
res = gauss.expectation_maximization(data)
print res
