from pylab import *

x = linspace(0,10.,10)
y = linspace(0,10.,10)
x,y = meshgrid(x,y)
u = x*10
v = np.zeros(y.shape)
q = plt.quiver(x,y,u,v,angles='xy',scale=1000,color='r')
p = plt.quiverkey(q,1,16.5,50,"50 m/s",coordinates='data',color='r')


plt.show()
