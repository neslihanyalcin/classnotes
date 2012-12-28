import numpy as np
import itertools

def dist(vect,x):
    return np.fromiter(itertools.imap(np.linalg.norm, vect-x),dtype=np.float)

def norm(x,y): return np.linalg.norm(x-y)

if __name__ == "__main__": 
    points = np.array([[3.,3.],[2.,2.]])
    print "points", points
    q = [1.,1.]
    print "to", q
    print "diff", points-q
    print "dist", dist(points,q)
