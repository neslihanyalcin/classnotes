from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawValueProtocol
from mrjob.protocol import RawProtocol
import numpy as np, sys, itertools
from scipy import sparse
import random, common

class MRProj(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def configure_options(self):
        super(MRProj, self).configure_options()
        self.add_passthrough_option('--k')
        
    def __init__(self, *args, **kwargs):
        super(MRProj, self).__init__(*args, **kwargs)
        
    def mapper(self, key, line):
        line_sps = common.line_to_coo(line, 17770)
        result = np.zeros(int(self.options.k))
        for xx,j,v in itertools.izip(line_sps.row, line_sps.col, line_sps.data):
            np.random.seed(j)
            result += v*np.random.randn(int(self.options.k))
        yield int(key), ";".join(map(str,result))
            
if __name__ == '__main__':
    MRProj.run()
