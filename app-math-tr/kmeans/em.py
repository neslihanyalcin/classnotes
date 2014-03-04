import numpy as np, math, itertools
import numpy.linalg as linalg
import matplotlib.pylab as plt

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

def plot(data, mus, sigmas):
  plt.scatter (data[:,1],data[:,2])
  plt.hold(True)
  plt.xlim(55,80)
  plt.ylim(80,280)

  x = np.arange(55., 80., 2)
  y = np.arange(80., 280., 2)
  X, Y = np.meshgrid(x, y)

  Z = np.zeros(X.shape)
  nx, ny = X.shape
  for mu,sigma in itertools.izip(mus,sigmas):
    for i in xrange(nx):
        for j in xrange(ny):
            Z[i,j] = norm_pdf(np.array([X[i,j], Y[i,j]]),mu,sigma)
    levels = np.linspace(Z.min(), Z.max(), 4)
    plt.contour(X, Y, Z, colors='k', levels=levels)
    plt.hold(True)
  #plt.show()
  plt.hold(False)
  

#mu1 = np.array([  100.,  100.])
#mu2 = np.array([  110.,  110.  ])
mu1 = np.array([  65.,  200])
mu2 = np.array([  72.,  200  ])
#sigma1 = sigma2 = np.matrix([[  400.,    0],[ 0.,  400.]])
sigma1 = sigma2 = np.matrix([[  7,    10],[ 10,  500]])

mus = []; mus.append(mu1); mus.append(mu2)
sigmas = []; sigmas.append(sigma1); sigmas.append(sigma2)

iter = 20
k = len(mus)
data = np.loadtxt('biometric_data_simple.txt',delimiter=',')
n = len(data)
gamma = np.zeros((n,k))
pi = np.ones(k)*(1./k)
print pi
                   
for it in range(iter):
  if it % 5 == 0:
    plot(data, mus, sigmas)
    plt.savefig("/tmp/out-%d.png" % it)
  print it
  # E-basamagi
  for j in range(k):
    for i in range(n):
      gamma[i,j] = norm_pdf(data[i,1:],mus[j],sigmas[j])*pi[j]
  gamma = np.array(map(lambda x: x / np.sum(x), gamma))
  print gamma
  for j in range(k):
    #mus[j] = np.zeros(mus[j].shape)
    #sigmas[j] = np.matrix(np.zeros(sigmas[j].shape))
    #sigmas[j][0,0] = 100.
    for i in range(n):
      mus[j] += data[i,1:]*gamma[i,j]
    mus[j] = mus[j] / np.sum(gamma[:,j])
    for i in range(n):
      tmp = data[i,1:]-mus[j]
      sigmas[j] += np.dot(tmp,tmp.T)*gamma[i,j] 
    sigmas[j] = sigmas[j] / np.sum(gamma[:,j])
  print 'mu',mus
  print 'sigma',sigmas
        