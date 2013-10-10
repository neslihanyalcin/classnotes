from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawProtocol
import numpy as np, sys
from scipy import sparse
import random

class MRAtQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRAtQ, self).__init__(*args, **kwargs)

    def mapper(self, key, line):
        yield key, line

    def reducer(self, key, value):
        for val in value:
            print key, "-", val
        
if __name__ == '__main__':
    MRAtQ.run()
