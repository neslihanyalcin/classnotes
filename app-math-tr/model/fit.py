import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(t,A,k,K):
    return K / (1+A*np.exp(-k*t))    

def resid(p, y, t):
    A,k,K = p
    return y - f(t,A,k,K)

if __name__ == '__main__':
    t, x1 = np.loadtxt('population.txt', unpack=True)
    y1 = np.log(x1)
    
    A0,k0,K0 = 1, 1, 1
    [A,k,K], flag  = optimize.leastsq(resid, [A0,k0,K0], 
                                           args=(y1, t))


    print flag, A,k,K
        
    t = np.linspace(0,10,100)
    plt.plot(t, f(t,A,k,K))
    plt.hold(True)        
    
    
    plt.show()
