import numpy as np
from EMmixtureBernoulli import *
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

K=3
iter=20
Y = np.loadtxt('binarydigits.txt')

attempts=20
Lbest = -np.inf
eps=1e-15
for attempt in range(attempts):
    lRtmp,lPitmp,lPtmp,L,iters = EMmixtureBernoulli(Y,K,iter,eps)
    if L[iters]>Lbest:
        lR=lRtmp
        lPi=lPitmp
        lP=lPtmp
        Lbest=L[iters]
        itersbest=iters

print lR
print lPi
print lP

    
