from sasha import job
import numpy as np, sys, itertools
from scipy import sparse
import random, re, sys, proj
import numpy.linalg as lin

'''
We calculate the matrix multiplication A transpose Q (AtQ) where A and
Q have m rows (large), n and k rows (large and small respectively).
'''
class AtQ(job.SashaJob):
    
    def __init__(self):
        job.SashaJob.__init__(self)
        self.mat_sum = np.zeros(proj.K)
        
    def mapper(self, id, line):
        [a, q] = line.split("|")
        left = proj.key_val_to_coo(a, proj.N)
        right = np.array(map(np.float,q.split(';')))
        # iterate only non-zero elements in the bigger (left) vector
        for i,j,v in zip(left.row, left.col, left.data):
            out = ";".join(map(str,np.round(v*right,3)))
            yield str(j), out

    def reducer(self, val):
        val = np.fromstring(val, sep=';')
        self.mat_sum += np.array(val)

    def result(self):
        yield ";".join(map(lambda x: str(np.round(x,3)),self.mat_sum))

        
if __name__ == "__main__":    
    AtQ.run()
