import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import time    

if __name__ == "__main__": 
 points = np.array([[3.,4.],[5.,5.],[9.,2.],[3.2,5.],[7.,5.],
                  [8.,9.],[7.,6.],[8,4],[6,2],[2,2],[4,8]])
 f = plt.figure()
 ax = f.gca()
 ax.plot(points,'ko')
 c = Circle([5, 5], 5)
 ax.add_patch(c)
 plt.show()
