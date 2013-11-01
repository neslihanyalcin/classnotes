from sasha import job
import numpy as np, sys, itertools
from scipy import sparse
import random, re, sys

N = 30; K = 7
#N = 3730; K = 7

def key_val_to_coo(line, dim):
    line_sps = sparse.lil_matrix((1,dim))
    tokens = line.split(";")
    for tok in tokens:
        [id,val] = tok.split(":")
        line_sps[0,long(id)] = np.float(val)
    return line_sps.tocoo()

class MRProj(job.SashaJob):
    
    def __init__(self):
        job.SashaJob.__init__(self)
            
    def mapper(self, key, line):
        line_sps = key_val_to_coo(line, N)
        result = np.zeros(K)
        for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
            np.random.seed(j)
            result += v*np.random.randn(K)
            
        yield key, ";".join(map(lambda x: str(np.round(x,3)),result))
        
if __name__ == "__main__":    
    MRProj.run()
