import matplotlib.pyplot as plt
import numpy as np
import time

def form_tree(points):
    while True:
        plt.ion()
        time.sleep(1)
        plt.hold(False)
        points += 0.3
        plt.xlim(0,20)
        plt.ylim(0,20)
        plt.plot(points,'x')
        plt.draw()
        print points
    

if __name__ == "__main__": 
 test = np.array([[3,4],[5,5],[9,2],[3.2,5],[7,5],[8,9],[7,6]])
 form_tree(test)
