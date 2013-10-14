from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawProtocol
from mrjob.protocol import RawValueProtocol
import numpy as np, sys, common
from scipy import sparse
import random

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
        
    def __init__(self, *args, **kwargs):
        super(MRAtQ, self).__init__(*args, **kwargs)

    '''
    No mapper, only reducer in the first step. W/out mapper, two lines
    (and there are only two lines, per key -one from A one from Q-)
    with same key will end up in same reducer.
    '''
    def reducer(self, key, value):
        left = None; right = None
        for i,line in enumerate(value):
            if ':' in line:
                left = common.line_to_coo(line, 17770)
            else:
                line = line.replace('"','')
                line_vals = map(lambda x: float(x or 0), line.split(';'))
                right = np.array(line_vals)
        
        # iterate only non-zero elements in the bigger (left) vector
        for i,j,v in zip(left.row, left.col, left.data):
            mult = v*right
            yield j, mult

    '''
    In the second step, again no mapper one reducer, there is a sum,
    for all ith \elem n vectors that were multiplied in the previous
    step
    '''
    def reduce_sum(self, key, value):
        mat_sum = np.zeros((1,int(self.options.k)))
        for val in value: mat_sum += val
        yield (int(key), ";".join(map(str,mat_sum[0])))
            
    def steps(self):
        return [
            self.mr(reducer=self.reducer),
            self.mr(reducer=self.reduce_sum)
        ]

            
if __name__ == '__main__':
    MRAtQ.run()