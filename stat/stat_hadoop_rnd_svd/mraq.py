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
        
    def reducer(self, key, value):
        for i,line in enumerate(value):
            line = line.replace('"','')
            #print line
            line_vals = map(lambda x: float(x or 0), line.split(';'))
            print key, len(line_vals)

#    def steps(self):
#        return [
#            self.mr(reducer=self.reducer),
#            self.mr(reducer=self.reducer_find_max_word)
#        ]

            
if __name__ == '__main__':
    MRAtQ.run()
