import matplotlib.pyplot as plt
import numpy as np
import time
    

if __name__ == "__main__": 
    test = np.array([[3.,4.],[5.,5.],[9.,2.],[3.2,5.],[7.,5.],
                     [8.,9.],[7.,6.],[8,4],[6,2],[2,2],[4,8]])
    for x in test: plt.plot(x[0],x[1],'ko')
    plt.xlim(-10,20)
    plt.ylim(-10,20)
    plt.show()
