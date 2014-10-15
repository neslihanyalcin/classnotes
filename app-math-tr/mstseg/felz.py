import scipy.sparse as sps
import scipy.io as io
import itertools

def threshold(size, c): return c / size 

class Felzenswalb:
    def __init__(self, t):
        self.t_ = t

    def fit(self, X):        
        E = [(v,i,j) for i,j,v in itertools.izip(X.row, X.col, X.data)]
        E = list(sorted(E))
        C = {u[1]:u[1] for u in E}
        print C
        ts = {x:threshold(1,self.t_) for x in C}
        print ts
        for (v,i,j) in E:
            print v,i,j
    
