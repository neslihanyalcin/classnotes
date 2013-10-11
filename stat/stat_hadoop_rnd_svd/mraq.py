from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawProtocol
from mrjob.protocol import RawValueProtocol
import numpy as np, sys
from scipy import sparse
import random

class MRAtQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRAtQ, self).__init__(*args, **kwargs)
        self.n = 5

    def reducer(self, key, value):
        v = []
        for i,line in enumerate(value):
            line = line.replace('"','')
            line_vals = map(lambda x: float(x or 0), line.split(';'))
            v.append(np.array(line_vals))

        left = v[np.argmax(map(len, v))]
        left = sparse.coo_matrix(left)
        right = v[np.argmin(map(len, v))]
        right = sparse.coo_matrix(right)
        
        for i,j,v in zip(left.row, left.col, left.data):
            mult = v*right
            yield j, mult.todense()[0]

    def reduce_sum(self, key, value):
        mat_sum = np.zeros((1,self.n))
        for val in value: mat_sum += val
        yield (float(key), ";".join(map(str,mat_sum[0])))
            
    def steps(self):
        return [
            self.mr(reducer=self.reducer),
            self.mr(reducer=self.reduce_sum)
        ]

            
if __name__ == '__main__':
    MRAtQ.run()
