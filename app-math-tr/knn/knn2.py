import matplotlib.pyplot as plt
import numpy as np
import time

__rmin__ = 2

def dist(vect,x):
    return np.sum(np.abs(x-vect),axis=1)

#
# node = [pivot, radius, points, [child1,child2]]
#
def form_tree(points,node):
    pivot = points[0]
    print "pivot",pivot
    radius = np.max(dist(points,pivot))
    node[0] = pivot
    node[1] = radius
    if len(points) <= __rmin__:
        node[2] = points
        return
    print "node",node
    idx = np.argmax(dist(points,pivot))
    furthest = points[idx,:]
    print "new pivot 1", furthest
    idx = np.argmax(dist(points,furthest))
    furthest2 = points[idx,:]
    print "new pivot 2", furthest2
    dist1=dist(points,furthest)
    dist2=dist(points,furthest2)
    diffs = dist1-dist2
    print "points",points
    print diffs
    p1 = points[diffs <= 0]
    p2 = points[diffs > 0]
    print "points 1", p1
    print "points 2", p2
    node[3][0] = [None,None,None,[None,None]]
    node[3][1] = [None,None,None,[None,None]]
    form_tree(p1,node[3][0])
    form_tree(p2,node[3][1])
                    

if __name__ == "__main__": 
    test = np.array([[3.,4.],[5.,5.],[9.,2.],[3.2,5.],[7.,5.],[8.,9.],[7.,6.],
                     [8,4],[6,2]])
    tree = [None,None,None,[None,None]]
    form_tree(test,tree)
    print tree
