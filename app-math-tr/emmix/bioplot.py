import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('biometric_data_simple.txt',delimiter=',')

women = data[data[:,0] == 1]
men = data[data[:,0] == 2]

plt.plot (women[:,2],women[:,1], 'b.')
plt.hold(True)
plt.plot (men[:,2],men[:,1], 'r.')
plt.show()
