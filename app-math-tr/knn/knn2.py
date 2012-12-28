import matplotlib.pyplot as plt
import pprint
import numpy as np
import time
import dist

__rmin__ = 2

# node: [pivot, radius, points, [child1,child2]]
def new_node(): return  [None,None,None,[None,None]]

def form_tree(points,node):
    pivot = points[0]
    print "pivot",pivot
    radius = np.max(dist.dist(points,pivot))
    node[0] = pivot
    node[1] = radius
    if len(points) <= __rmin__:
        node[2] = points
        return
    print "node",node
    idx = np.argmax(dist.dist(points,pivot))
    furthest = points[idx,:]
    print "new pivot 1", furthest
    idx = np.argmax(dist.dist(points,furthest))
    furthest2 = points[idx,:]
    print "new pivot 2", furthest2
    dist1=dist.dist(points,furthest)
    dist2=dist.dist(points,furthest2)
    diffs = dist1-dist2
    print "points",points
    print diffs
    p1 = points[diffs <= 0]
    p2 = points[diffs > 0]
    print "points 1", p1
    print "points 2", p2
    node[3][0] = new_node() # left child
    node[3][1] = new_node() # right child
    form_tree(p1,node[3][0])
    form_tree(p2,node[3][1])

# knn: [min_so_far, [points]]
def search_tree(new_point, knn, node):
    print "c",node[0]
    print "r",node[1]
    print "np", new_point    
    node_min = dist.norm(node[0],new_point) - node[1]
    print "node_min",node_min
       
if __name__ == "__main__": 
    test = np.array([[3.,4.],[5.,5.],[9.,2.],[3.2,5.],[7.,5.],
                     [8.,9.],[7.,6.],[8,4],[6,2]])
    tree = new_node()
    form_tree(test,tree)
    pp = pprint.PrettyPrinter(indent=4)
    print "\ntree"
    pp.pprint(tree)
    print search_tree(np.array([5.,5.]),[np.Inf, []], tree)
    
