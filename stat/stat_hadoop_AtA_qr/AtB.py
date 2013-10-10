from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawProtocol
import numpy as np, sys
from scipy import sparse
import random

class MRAtB(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRAtB, self).__init__(*args, **kwargs)

#    def mapper(self, key, line):
#        yield key, line

    def reducer(self, key, value):
        l = list(value)
        print len(l[0]), len(l[1])
#        print self
#        for val in value:
#            print key, "-", val
        
if __name__ == '__main__':
    MRAtB.run()
