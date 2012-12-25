import matplotlib.pyplot as plt
import numpy as np
import time

def dist(vect,x):
    return np.sum(np.abs(x-vect),axis=1)

# node = [centroid, radius, (child1,child2)]
def form_tree(points,node):
    center = np.mean(points,axis=0)
    print "center",center
    idx = np.argmax(dist(points,center))
    furthest = points[idx,:]
    print furthest
    idx = np.argmax(dist(points,furthest))
    furthest2 = points[idx,:]
    print furthest2

if __name__ == "__main__": 
    test = np.array([[3.,4.],[5.,5.],[9.,2.],[3.2,5.],[7.,5.],[8.,9.],[7.,6.],
                     [8,4],[6,2]])
    form_tree(test,[])
