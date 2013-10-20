from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawProtocol
from mrjob.protocol import RawValueProtocol
from mrjob.protocol import JSONProtocol
from mrjob.protocol import ReprProtocol
import numpy as np, sys
from scipy import sparse
import random, mrc

'''
We feed two files into this job, A and Q, then we calculate the matrix
multiplication A transpose Q (AtQ) where A and Q have m rows (large),
n and k rows (large and small respectively). 
'''
class MRAtQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def configure_options(self):
        super(MRAtQ, self).configure_options()
        self.add_passthrough_option('--k')
        self.add_passthrough_option('--n')
        
    def __init__(self, *args, **kwargs):
        super(MRAtQ, self).__init__(*args, **kwargs)
                    
    '''
    Two lines per key -one from A one from Q- with same key will arrive
    in the same reducer.
    '''
    def reducer(self, key, two_lines):
        left = None; right = None
        for line in two_lines:
            line = line.replace('"','')
            if ':' in line:
                left = mrc.line_to_coo(line, int(self.options.n))
            else:
                right = np.array(map(lambda x: np.float(x), line.split(';')))
        
        # iterate only non-zero elements in the bigger (left) vector
        for i,j,v in zip(left.row, left.col, left.data):
            yield j, ";".join(map(str,np.round(v*right,3)))

    '''
    In the second step, again no mapper one reducer, there is a sum,
    for all ith \elem n vectors that were multiplied in the previous
    step
    '''
    def reduce_sum(self, key, value):
        mat_sum = np.zeros((1,int(self.options.k)))
        for val in value:
            val = np.fromstring(val, sep=';')
            mat_sum += val
        yield (int(key), ";".join(map(lambda x: str(np.round(x,3)),mat_sum[0]) ))
            
    def steps(self):
        return [
            self.mr(reducer=self.reducer),
            self.mr(reducer=self.reduce_sum)
        ]

            
if __name__ == '__main__':
    MRAtQ.run()
