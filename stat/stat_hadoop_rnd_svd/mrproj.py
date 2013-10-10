from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
import numpy as np, sys, itertools
from scipy import sparse
import random

class MRProj(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRProj, self).__init__(*args, **kwargs)
        self.k = 7

    def mapper(self, key, line):
        line_vals = map(lambda x: float(x or 0), line.split(';'))
        key = line_vals[0]
        line_vals = line_vals[1:]
        line_sps = sparse.coo_matrix(line_vals,shape=(1,len(line_vals)))
        result = np.zeros(self.k)
        for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
            for i in range(self.k):
                random.seed(int(j + i))
                result[i] += v*random.gauss(0,1)
        yield (None,",".join(map(str,result)))
            
if __name__ == '__main__':
    MRProj.run()
