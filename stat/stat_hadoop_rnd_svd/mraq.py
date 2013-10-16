from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawProtocol
from mrjob.protocol import RawValueProtocol
import numpy as np, sys
from scipy import sparse
import random, mrc
import UserString

class MRAtQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def configure_options(self):
        super(MRAtQ, self).configure_options()
        self.add_passthrough_option('--k')
        self.add_passthrough_option('--n')
        
    def __init__(self, *args, **kwargs):
        super(MRAtQ, self).__init__(*args, **kwargs)

    def mapper(self, key, value):
        tokens = value.split('\t')
        Q = tokens[0].replace('"','')
        A = tokens[2]
        Q = map(lambda x: float(x or 0), Q.split(';'))
        A = mrc.line_to_coo(A, int(self.options.n))
        # iterate only non-zero elements of A
        for i,j,v in zip(A.row, A.col, A.data):
            yield j, v*Q

    def reducer(self, key, value):
        mat_sum = np.zeros((1,int(self.options.k)))
        for val in value: mat_sum += val
        yield (int(key), ";".join(map(str,mat_sum[0])))
            
if __name__ == '__main__':
    MRAtQ.run()
