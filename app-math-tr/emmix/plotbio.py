import scipy.stats
import numpy as np
import pnorm
import matplotlib.pyplot as plt
data = np.loadtxt('biometric_data_simple.txt',delimiter=',')

women = data[data[:,0] == 1]
men = data[data[:,0] == 2]

plt.xlim(55,80)
plt.ylim(80,280)
plt.plot (women[:,1],women[:,2], 'b.')
plt.hold(True)
plt.plot (men[:,1],men[:,2], 'r.')
plt.xlabel('height (inch)')
plt.ylabel('weight (pound)')
plt.hold(True)

x = np.arange(55., 80., 1)
y = np.arange(80., 280., 1)
X, Y = np.meshgrid(x, y)

Z = np.zeros(X.shape)
nx, ny = X.shape

def norm_pdf(b,mean,cov):
   k = b.shape[0]
   part1 = np.exp(-0.5*k*np.log(2*np.pi))
   part2 = np.power(np.linalg.det(cov),-0.5)
   dev = b-mean
   part3 = np.exp(-0.5*np.dot(np.dot(dev.transpose(),np.linalg.inv(cov)),dev))
   dmvnorm = part1*part2*part3
   return dmvnorm

for i in xrange(nx):
    for j in xrange(ny):
        Z[i,j] = norm_pdf(np.array([X[i,j], Y[i,j]]),
                       np.array([  72.89350086,  193.21741426]),
                       np.matrix([[    7.84711283,    25.03111826],
                                  [   25.03111826,  1339.70289046]]))
        
plt.contour(X, Y, Z, colors='k')

plt.show()
