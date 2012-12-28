from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import pprint
import numpy as np
import time
import dist

__rmin__ = 2

# node: [pivot, radius, points, [child1,child2]]
def new_node(): return  [None,None,None,[None,None]]

def circle(x,rad,ax):
    c = Circle([x[0], x[1]], rad, color='lightgreen')
    ax.add_patch(c)
    plt.xlim(-10,20)
    plt.ylim(-10,20)

def plot_points(pts,color,ax):
    for x in pts: ax.plot(x[0],x[1],color)
    
def form_tree(points,node,all_points):
    global i
    print 'entering form tree ---'
    print "points",points
    pivot = points[0]
    print "pivot",pivot
    radius = np.max(dist.dist(points,pivot))
    print "radius",radius
    f = plt.figure()
    ax = f.gca()
    plot_points(all_points,'ko',ax)
    plot_points(points,'ro',ax)
    circle(pivot,radius,ax)
    #plt.show()
    plt.savefig('knn%s.png' % str(i))
    i += 1
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
    form_tree(p1,node[3][0],all_points)
    form_tree(p2,node[3][1],all_points)
       
if __name__ == "__main__":
    i = 0
    points = np.array([[3.,4.],[5.,5.],[9.,2.],[3.2,5.],[7.,5.],
                       [8.,9.],[7.,6.],[8,4],[6,2]])
    tree = new_node()
    form_tree(points,tree,points)
    pp = pprint.PrettyPrinter(indent=4)
    print "\ntree"
    pp.pprint(tree)
    
