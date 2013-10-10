from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
import numpy as np, sys
import numpy.linalg as lin

'''
Q = A*inv(R) should be calculated
'''
class MRQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRQ, self).__init__(*args, **kwargs)
        self.R_inv = lin.inv(np.loadtxt('R'))
        self.data = []
        self.buffer_size = 4
        
    def mapper(self, key, line):
        line_vals = map(np.float,line.split(','))
        self.data.append(line_vals)
        if len(self.data) == self.buffer_size:
            mult = np.dot(self.data,self.R_inv)
            self.data = []
            for x in mult:
                yield (key,",".join(map(str,x)))
        
if __name__ == '__main__':
    MRQ.run()

