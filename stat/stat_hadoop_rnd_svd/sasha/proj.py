from sasha import job
import numpy as np, sys, itertools
import scipy.sparse as sps
import random, re, sys

N = 30; K = 7
#N = 3730; K = 7

def key_val_to_coo(line, dim):
    line_sps = sps.lil_matrix((1,dim))
    ids = re.findall("(\d+):(\d+)",line)
    def f(x): line_sps[0,long(x[0])] = np.float(x[1])
    map(f, ids)
    return line_sps.tocoo()

class Proj(job.SashaJob):
        
    def __init__(self):
        job.SashaJob.__init__(self)
        self.randoms = {}
            
    def mapper(self, key, line):
        line_sps = key_val_to_coo(line, N)
        result = np.zeros(K)
        for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
            if j not in self.randoms: 
                np.random.seed(j)
                self.randoms[j] = np.random.randn(K) 
            result += v*self.randoms[j]
        yield key, ";".join(map(lambda x: str(np.round(x,3)),result))
                    
if __name__ == "__main__":    
    Proj.run()
