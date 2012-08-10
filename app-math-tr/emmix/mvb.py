import numpy as np
from EMmixtureBernoulli import *
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

K=3
iter=20
Y = np.loadtxt('binarydigits.txt')

#for i in range(100):
#    plt.imshow(Y[i,:].reshape((8,8),order='F'), cmap=plt.cm.gray)
#    plt.show()

attempts=20
Lbest = -np.inf
eps=1e-15
for attempt in range(attempts):
    EMmixtureBernoulli(Y,K,iter,eps)
    
