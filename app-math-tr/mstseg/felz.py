import scipy.sparse as sps
import scipy.io as io
import itertools, numpy as np

def threshold(size, c): return c / size 

S = {}

def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])                    # Path compression
    return C[u]

def union(C, R, u, v, S):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:                             # Union by rank
        C[v] = u
        S[v] = S[u] + S[v]
        S[u] = S[u] + S[v]
    else:
        C[u] = v
        tmp = S[u] + S[v]
        S[u] = tmp
        S[v] = tmp
    if R[u] == R[v]:                            # A tie: Move v up a level
        R[v] += 1

class Felzenswalb:
    def __init__(self, threshold, c):
        self.threshold_ = threshold
        self.c_ = c

    def fit(self, X):
        print X.shape
        G = {}
        for i in range(X.shape[0]): G[i] = {}
        for u,v,w in itertools.izip(X.row, X.col, X.data): G[u][v] = w
        E = [(G[u][v],u,v) for u in G for v in G[u]]
        E = sorted(E)        
        T = set()
        C, R = {u:u for u in G}, {u:0 for u in G}   # Comp. reps and ranks
        S = {u:1 for u in range(len(G))}
        
        ts = {x:threshold(1,self.c_) for x in C}
        
        for w, u, v in E:
            if find(C, u) != find(C, v):
                if w <= ts[u] and w <= ts[v]:
                    T.add((u, v))
                    union(C, R, u, v, S)
                    ts[u] = w + threshold(S[u],self.c_)
                                        
        self.labels_ = [np.nan for i in range(len(C))]
        for i in range(len(C)): self.labels_[i] = int(C[i])
        self.T_ = T
        
import scipy.sparse as sps
import scipy.io as io
X = io.mmread('simple.mtx')
clf = Felzenswalb(threshold=1,c=1.0)
clf.fit(X)
print clf.labels_    
