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
        
    def mapper(self, id, line):
        [a, q] = line.split("|")
        left = proj.key_val_to_coo(a, proj.N)
        right = proj.key_val_to_coo(a, proj.K).todense()
        # iterate only non-zero elements in the bigger (left) vector
        for i,j,v in zip(left.row, left.col, left.data):
            out = ";".join(map(str,np.round(v*right,3)))
            yield j, out
                        
if __name__ == "__main__":    
    AtQ.run()
