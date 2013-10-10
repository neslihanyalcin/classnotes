from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
from mrjob.protocol import RawProtocol
import numpy as np, sys
import numpy.linalg as lin

'''
Q = A*inv(R) should be calculated
'''
class MRQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRQ, self).__init__(*args, **kwargs)
        self.R_inv = lin.inv(np.loadtxt('R',delimiter=';'))
        
    def mapper(self, key, line):
        line = line.replace('"','')
        line_vals = map(np.float,line.split(';'))
        mult = np.dot(line_vals,self.R_inv)
        yield (float(key),";".join(map(str,mult)))
        
if __name__ == '__main__':
    MRQ.run()

