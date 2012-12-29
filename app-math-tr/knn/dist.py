import numpy as np
import itertools

def dist(vect,x):
    return np.fromiter(itertools.imap
                       (np.linalg.norm, vect-x),dtype=np.float)

def norm(x,y): return np.linalg.norm(x-y)

if __name__ == "__main__":
    # small test
    points = np.array([[3.,3.],[2.,2.]])
    q = [1.,1.]
    print "diff", points-q
    print "dist", dist(points,q)
