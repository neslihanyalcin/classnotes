from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
from mrjob.protocol import PickleProtocol, RawProtocol
import numpy as np, sys
import numpy.linalg as lin

'''
Calculate AtA then Cholesky to get R
'''
class MRR(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRR, self).__init__(*args, **kwargs)
        self.buffer_size = 4
        self.n = 7
        self.data = []
        self.A_sum = np.zeros((self.n,self.n))
        
    def mapper(self, key, line):
        line = line.replace('"','')
        line_vals = map(np.float,line.split(';'))
        self.data.append(line_vals)
        if len(self.data) == self.buffer_size:
            mult = np.dot(np.array(self.data).T,np.array(self.data))
            self.data = []
            for i, val in enumerate(mult):
                yield i, val        

    def mapper_final(self):        
        if len(self.data) > 0:
            mult = np.dot(np.array(self.data).T,np.array(self.data))
            for i, val in enumerate(mult):
                yield i, val
    
    def reducer(self, i, tokens):
        for val in tokens:
            self.A_sum[i,:] += np.array(val)        
    
    def reducer_final(self):
        for x in lin.cholesky(self.A_sum).T:            
            yield (None,";".join(map(str,x)))
        
if __name__ == '__main__':
    MRR.run()

