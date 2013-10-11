from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
from mrjob.protocol import PickleProtocol, RawProtocol
import numpy as np, sys
import numpy.linalg as lin

class MRUR(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def configure_options(self):
        super(MRUR, self).configure_options()
        self.add_file_option('--R')
        
    def __init__(self, *args, **kwargs):
        super(MRUR, self).__init__(*args, **kwargs)
        Ur,x,x = lin.svd(np.loadtxt(self.options.R,delimiter=';'))
        self.Ur = Ur
        self.data = []
        self.buffer_size = 4
        
    def mapper(self, key, line):
        line = line.replace('"','')
        line_vals = map(np.float,line.split(';'))
        self.data.append(line_vals)
        if len(self.data) == self.buffer_size:
            mult = np.dot(self.data,self.Ur)
            self.data = []
            for x in mult:
                yield (key,",".join(map(str,x)))
        
if __name__ == '__main__':
    MRUR.run()

