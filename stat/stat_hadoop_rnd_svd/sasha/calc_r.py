from sasha import job
import numpy as np, sys, itertools
from scipy import sparse
import random, re, sys, proj
import numpy.linalg as lin

'''
Calculate AtA then Cholesky to get R
'''
class CalcR(job.SashaJob):
    
    def __init__(self):
        job.SashaJob.__init__(self)
        self.buffer_size = 4
        self.data = [] # buffer for mapper
        self.row_sum = np.zeros((1,proj.K)) # reducer 
            
    def mapper(self, key, line):
        line_vals = map(np.float,line.split(';'))
        self.data.append(line_vals)
        if len(self.data) == self.buffer_size:
            mult = np.dot(np.array(self.data).T,np.array(self.data))
            self.data = []
            for i, val in enumerate(mult):
                val = ";".join(map(lambda x: str(np.round(x,3)),val))
                yield str(i), val

    def mapper_final(self):        
        if len(self.data) > 0:
            mult = np.dot(np.array(self.data).T,np.array(self.data))
            for i, val in enumerate(mult):
                val = ";".join(map(lambda x: str(np.round(x,3)),val))
                yield str(i), val

    def reducer(self, token):
        token = map(np.float,token.split(';'))
        self.row_sum += token
            
    def result(self):
        yield ";".join(map(lambda x: str(np.round(x,3)), self.row_sum))

                
if __name__ == "__main__":    
    CalcR.run()
