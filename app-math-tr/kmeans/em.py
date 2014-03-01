# Multivariate gaussian, contours
#
import numpy as np, math
import numpy.linalg as linalg
import matplotlib.pylab as plt
data = np.loadtxt('biometric_data_simple.txt',delimiter=',')

def norm_pdf(x, mu, sigma):
  size = len(x)
  if size == len(mu) and (size, size) == sigma.shape:
    det = linalg.det(sigma)
    if det == 0: raise NameError("The covariance matrix can't be singular")
    norm_const = 1.0/ ( math.pow((2*math.pi),float(size)/2) * math.pow(det,1.0/2) )
    x_mu = np.matrix(x - mu)
    inv = sigma.I        
    result = math.pow(math.e, -0.5 * (x_mu * inv * x_mu.T))
    return norm_const * result
  else:
     raise NameError("The dimensions of the input don't match")


plt.scatter (data[:,1],data[:,2])
plt.hold(True)
plt.xlim(55,80)
plt.ylim(80,280)

x = np.arange(55., 80., 2)
y = np.arange(80., 280., 2)
X, Y = np.meshgrid(x, y)

Z = np.zeros(X.shape)
nx, ny = X.shape
mu1 = np.array([  72.,  193.217])
sigma1 = np.matrix([[  7.84711,    10],[ 10,  1339.7028]])
for i in xrange(nx):
    for j in xrange(ny):
        Z[i,j] = norm_pdf(np.array([X[i,j], Y[i,j]]),mu1,sigma1)
        
        
levels = np.linspace(Z.min(), Z.max(), 4)

plt.contour(X, Y, Z, colors='k', levels=levels)
plt.hold(True)

Z = np.zeros(X.shape)
nx, ny = X.shape
mu2 = np.array([  66.,  135.308125  ])
sigma2 = np.matrix([[  14.28189396,   10],[  10,  403.09566456]])
for i in xrange(nx):
    for j in xrange(ny):
        Z[i,j] = norm_pdf(np.array([X[i,j], Y[i,j]]),mu2,sigma2)
        
levels = np.linspace(Z.min(), Z.max(), 4)

plt.contour(X, Y, Z, colors='k', levels=levels)
plt.show()
