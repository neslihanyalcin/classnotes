# Pure Halko
import numpy as np
import numpy.random as rand
import numpy.linalg as lin
import matplotlib.pyplot as plt
import pandas as pd

U = np.loadtxt('U_final.dat',delimiter=',')
plt.plot(U[:,0],U[:,1],'r+')
plt.hold(True)
        
n = 29
df = pd.read_csv("w1.csv",sep=';')
A = np.array(df)[:,1:]
U, Sigma, V = lin.svd(A);
plt.plot(U[:,0],U[:,1],'bx')
plt.show()
