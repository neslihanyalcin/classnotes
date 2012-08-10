import numpy as np

def logsumexp(a):
    return np.log(np.sum(np.exp(a), axis=0))

def EMmixtureBernoulli(Y,K,iter,tol):
    N,D=Y.shape
    print "N,K",N,K
    OMY=1+(-1*Y) #  "One minus Y", (1-Y)
    tmp=np.random.rand(N,K)
    tmp2=np.sum(tmp,axis=1).reshape((N,1))
    tmp3=np.tile(tmp2,(1,K))
    lR=np.log(np.divide(tmp, tmp3))
    for i in range(iter):
	lPi=np.tile(-1 * np.log(N),(K,1))+logsumexp(lR).T.reshape((K,1))  # lPi log Mixture params Kx1
        print lPi
        exit()
