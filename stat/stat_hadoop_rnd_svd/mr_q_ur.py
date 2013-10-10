from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
import numpy as np, sys
import numpy.linalg as lin

class MRUR(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRUR, self).__init__(*args, **kwargs)
        Ur,x,x = lin.svd(np.loadtxt('R'))
        self.Ur = Ur
        self.data = []
        self.buffer_size = 4
        
    def mapper(self, key, line):
        line_vals = map(np.float,line.split(','))
        self.data.append(line_vals)
        if len(self.data) == self.buffer_size:
            mult = np.dot(self.data,self.Ur)
            self.data = []
            for x in mult:
                yield (key,",".join(map(str,x)))
        
if __name__ == '__main__':
    MRUR.run()

