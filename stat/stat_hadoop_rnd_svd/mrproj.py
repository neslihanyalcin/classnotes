from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawValueProtocol
from mrjob.protocol import RawProtocol
import numpy as np, sys, itertools
from scipy import sparse
import random

'''
Random projection of matrix A. We key in seed generation to i,j
indexes so we dont have to store the random matrix itself.
'''
class MRProj(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRProj, self).__init__(*args, **kwargs)
        self.k = 7

    def mapper(self, key, line):
        line_vals = map(lambda x: float(x or 0), line.split(';'))
        line_vals = line_vals[1:]
        line_sps = sparse.coo_matrix(line_vals,shape=(1,len(line_vals)))
        result = np.zeros(self.k)
        for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
            for i in range(self.k):
                np.random.seed(int(j + i))
                result[i] += v * np.random.randn()
        yield (float(key), ";".join(map(str,result)))
            
if __name__ == '__main__':
    MRProj.run()
