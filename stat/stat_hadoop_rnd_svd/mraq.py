from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawProtocol
from mrjob.protocol import RawValueProtocol
import numpy as np, sys
from scipy import sparse
import random

class MRAtQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawValueProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRAtQ, self).__init__(*args, **kwargs)

    def mapper(self, key, line):
        line_vals = None
        if '\t' not in line: 
            line_vals = map(lambda x: float(x or 0), line.split(';'))
            #print len(line_vals)
            yield(key, line_vals)
        else:
            tmp = line.replace('"','').split('\t')
            line_vals = map(lambda x: float(x or 0), tmp[1].split(';'))
            #print len(line_vals)
            yield(tmp[0], line_vals)
        
#    def reducer(self, key, value):
#        l = list(value)
#        print len(l[0]), len(l[1])
#        for i,val in enumerate(value):
#            print i, key, "-", val

#    def steps(self):
#        return [
#            self.mr(reducer=self.reducer),
#            self.mr(reducer=self.reducer_find_max_word)
#        ]

            
if __name__ == '__main__':
    MRAtQ.run()
