import numpy as np
import math
import random

# samples indexes from a sequence of probability table
# based on those probabilities
def w_choice(lst):
    n = random.uniform(0, 1)
    for item, weight in enumerate(lst):
        if n < weight:
            break
        n = n - weight
    return item

#
# hyperparameters: a1, a2, b1, b2
#
def coal(n,x,init,a1,a2,b1,b2):
    nn=len(x)
    theta=init[0]
    lam=init[1]
    k = init[2]
    z=np.zeros((nn,))
    for i in range(n):
        ca = a1 + sum(x[0:k])
        theta = np.random.gamma(ca, 1/float(k + b1), 1) 
        ca = a2 + sum(x[(k+1):nn])
        lam = np.random.gamma(ca, 1/float(nn-k + b2), 1)
        for j in range(nn):
            z[j]=math.exp((lam-theta)*(j+1)) * (theta/lam)**sum(x[0:j])
        # sample
        zz = z / sum(z)
        k = w_choice(zz)
    print float(theta), float(lam), float(k)
        
if __name__ == "__main__":
        
    data = np.loadtxt("coal.txt")
    coal(1100, data, init=[1,1,30], a1=1,a2=1,b1=1,b2=1)
