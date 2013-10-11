# Pure Halko
import numpy as np
import numpy.random as rand
import numpy.linalg as lin
import matplotlib.pyplot as plt
import pandas as pd

'''
(70, 30) Y (70, 5) Q (70, 5)
BT (30, 5)V (5, 5) Uhat (5, 5)
U (70, 5)
'''

k = 7
df = pd.read_csv("w1.csv",sep=';',header=None)
A = np.array(df)[:,1:]
print "A",A.shape

# randomized SVD

Omega = rand.randn(A.shape[1],k)

Y = np.dot(A, Omega) 
#np.savetxt('w3_halko.dat',Y,fmt='%.2f')
print "Y", Y.shape

Q, R = lin.qr(Y) 
Q = np.loadtxt('/home/burak/Q.dat',delimiter=';')
#np.savetxt('q_halko.dat',Q,fmt='%.2f')

BT = np.dot(A.T, Q)
print BT
#BT = np.loadtxt('/home/burak/BT.dat',delimiter=';')

print "Q", Q.shape
print "BT", BT.shape

x, x, V = lin.svd(BT)
print 'V', V.shape
Uhat = V.T 

print "Uhat", Uhat.shape

U = np.dot(Q, Uhat) 
#np.savetxt('U_final_halko.dat',U,fmt='%.2f')

print "U", U.shape

plt.plot(U[:,0],-U[:,1],'r+')

plt.hold(True)
        
# compare with real SVD

U, Sigma, V = lin.svd(A);
plt.plot(U[:,0],U[:,1],'bx')

plt.show()
