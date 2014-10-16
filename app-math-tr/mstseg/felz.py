import scipy.sparse as sps
import scipy.io as io
import itertools

def threshold(size, c): return c / size 

def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])                    # Path compression
    return C[u]

def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:                             # Union by rank
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:                            # A tie: Move v up a level
        R[v] += 1

class Felzenswalb:
    def __init__(self, threshold):
        self.threshold_ = threshold

    def fit(self, X):
        print X.shape
        G = {}
        for i in range(X.shape[0]): G[i] = {}
        for u,v,w in itertools.izip(X.row, X.col, X.data): G[u][v] = w
        E = [(G[u][v],u,v) for u in G for v in G[u]]
        T = set()
        C, R = {u:u for u in G}, {u:0 for u in G}   # Comp. reps and ranks
        
        ts = {x:threshold(1,self.threshold_) for x in C}
        
        for _, u, v in sorted(E):
            print u, v
            if find(C, u) != find(C, v):
                T.add((u, v))
                print 'C1',C
                union(C, R, u, v)
                print 'C2',C
                
        #for (v,i,j) in E: print v,i,j

        print T
                
        return T
        
