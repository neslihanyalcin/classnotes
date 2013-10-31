from sasha import job
import numpy as np, sys, itertools
from scipy import sparse
import random, re, sys

def line_to_coo(line, dim):
    tokens = line.split(";")
    line_sps = sparse.lil_matrix((1,dim))
    for tok in tokens:
        tmp = tok.split(":"); line_sps[ 0,long(tmp[0]) ] = np.float(tmp[1])
    return line_sps.tocoo()

N = 30
K = 7

class MRProj(job.SashaJob):
    
    def __init__(self):
        job.SashaJob.__init__(self)
            
    def mapper(self, key, line):
        line_sps = line_to_coo(line, N)
        result = np.zeros(K)
        for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
            np.random.seed(j); result += v*np.random.randn(K)
        yield key, ";".join(map(lambda x: str(np.round(x,3)),result))
        
if __name__ == "__main__":    
    MRProj.run()
