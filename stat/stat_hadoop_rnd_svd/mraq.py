from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawProtocol
from mrjob.protocol import RawValueProtocol
import numpy as np, sys
from scipy import sparse
import random

'''
We feed two files into this job, A and Q we calculate AtQ
'''
class MRAtQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def configure_options(self):
        super(MRAtQ, self).configure_options()
        self.add_file_option('--n')
        
    def __init__(self, *args, **kwargs):
        super(MRAtQ, self).__init__(*args, **kwargs)

    '''
    No mapper only reducer. W/out mapper two lines with same key
    will end up in same reducer.
    '''
    def reducer(self, key, value):
        left = None; right = None
        v = []
        for i,line in enumerate(value):
            line = line.replace('"','')
            line_vals = map(lambda x: float(x or 0), line.split(';'))
            v.append(np.array(line_vals))
                        
        if len(v[0]) == int(self.options.n): left = v[1]; right = v[0]
        if len(v[1]) == int(self.options.n): left = v[0]; right = v[1]

        left = sparse.coo_matrix(left)
        right = sparse.coo_matrix(right)
        
        for i,j,v in zip(left.row, left.col, left.data):
            mult = v*right
            yield j, mult.todense()[0]

    '''
    Again no mapper one reducer, to sum up all i \elem n
    vectors that were multiplied above
    '''
    def reduce_sum(self, key, value):
        mat_sum = np.zeros((1,int(self.options.n)))
        for val in value: mat_sum += val
        yield (int(key), ";".join(map(str,mat_sum[0])))
            
    def steps(self):
        return [
            self.mr(reducer=self.reducer),
            self.mr(reducer=self.reduce_sum)
        ]

            
if __name__ == '__main__':
    MRAtQ.run()
