import matplotlib.pyplot as plt
import numpy as np
import random
prez = np.loadtxt("pres.txt",  usecols = (1,))

plt.xlim(0,120)
plt.ylim(0,60)

for i in prez:
    plt.plot(i,10.0,'rx')
    
for i in prez:
    jitter1 = random.random()*5.0
    jitter2 = random.random()*5.0
    plt.plot(i+jitter1, 30.0+jitter2, 'go')
        
plt.show()
