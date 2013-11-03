from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
from mrjob.protocol import PickleProtocol, RawProtocol
import numpy as np, sys
import numpy.linalg as lin

'''
Calculate AtA then Cholesky to get R
'''
class MRR(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    OUTPUT_PROTOCOL = RawValueProtocol
    
    def configure_options(self):
        super(MRR, self).configure_options()
        self.add_passthrough_option('--k')
        
    def __init__(self, *args, **kwargs):
        super(MRR, self).__init__(*args, **kwargs)
        self.buffer_size = 4
        self.data = []
        self.A_sum = np.zeros((int(self.options.k),int(self.options.k)))
        
    def mapper(self, key, line):
        line = line.replace('"','')
        line_vals = map(np.float,line.split(';'))
        self.data.append(line_vals)
        if len(self.data) == self.buffer_size:
            mult = np.dot(np.array(self.data).T,np.array(self.data))
            self.data = []
            for i, val in enumerate(mult):
                yield i, val        

    def mapper_final(self):        
        if len(self.data) > 0:
            mult = np.dot(np.array(self.data).T,np.array(self.data))
            for i, val in enumerate(mult):
                yield i, val
    
    def reducer(self, i, tokens):
        for val in tokens:
            self.A_sum[i,:] += np.array(val)        
    
    def reducer_final(self):
        for row in lin.cholesky(self.A_sum).T:            
            yield (None,";".join(map(lambda x: str(np.round(x,3)),row) ))
        
if __name__ == '__main__':
    MRR.run()
