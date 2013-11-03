from sasha import job
import numpy as np, sys, itertools
import scipy.sparse as sps
import random, re, sys

#N = 30; K = 7
N = 3730; K = 7; BUFFER = 100

def key_val_to_coo(line, dim):
    line_sps = sps.lil_matrix((1,dim))
    ids = re.findall("(\d+):(\d+)",line)
    def f(x): line_sps[0,long(x[0])] = np.float(x[1])
    map(f, ids)
    return line_sps.tocoo()

class Proj(job.SashaJob):

    def reset(self):
        self.count = 0
        self.keys = []
        self.data = sps.lil_matrix((BUFFER, N))
        self.randoms = sps.lil_matrix((N, K))
        
    def __init__(self):
        job.SashaJob.__init__(self)
        self.reset()
        
    def mapper(self, key, line):
        line_sps = key_val_to_coo(line, N)
        self.data[self.count,:] = line_sps            
        for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
            if self.randoms[j,0] > 0: pass
            else:
                np.random.seed(j)
                self.randoms[j,:] = np.random.randn(K)                
        self.keys.append(key)
        self.count += 1        
        if self.count == BUFFER:
            mult = self.data * self.randoms
            for i,row in enumerate(mult.todense()):
                curr_row = row.tolist()[0]
                yield self.keys[i], ";".join(map(lambda x: str(np.round(x,3)),curr_row))
            self.reset()
            
    def mapper_final(self):
        for i in range(self.count):
            line_sps = self.data.tocoo()
            result = np.zeros(K)
            for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
                np.random.seed(j)
                result += v*np.random.randn(K) 
            yield self.keys[i], ";".join(map(lambda x: str(np.round(x,3)),result))

                    
if __name__ == "__main__":    
    Proj.run()
