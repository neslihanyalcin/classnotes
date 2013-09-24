import numpy as np
import scipy.linalg as lin
import matplotlib.pyplot as plt
import ktbc

K,T,B,C = ktbc.ktbc(3); print T

h = 1./4.

discrete = lin.solve( (1./h)**2 * T, [1.,1.,1.] )

discrete = np.insert(discrete, 0, discrete[0]) 
discrete = np.append(discrete, 0.) 

K,T,B,C = ktbc.ktbc(4); print T

discrete_2 = lin.solve( (1./h**2)*T, [1./2.,1.,1.,1.] )
# add little diff for plotting
# grafik ust uste binmesin diye azicik fark ekledik
discrete_2 = discrete_2 + 0.01 
discrete_2 = np.append(discrete_2, 0.) 

def u(x): return (1./2.)*(1. - x**2)

p1 = plt.plot([u(0.0), u(0.25), u(0.5), u(0.75), u(1.)])

p2 = plt.plot(discrete)

p3 = plt.plot(discrete_2)

plt.legend([p1,p2,p3], ["analytical solution (analitik cozum)",
                        "discrete solution 1 (ayriksal cozum 1)",
                        "discrete solution 2 (ayriksal cozum 2)"
                        ])

plt.show()

         
