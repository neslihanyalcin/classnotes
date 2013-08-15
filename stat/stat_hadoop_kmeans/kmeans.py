from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawProtocol
import numpy as np, sys
import pandas as pd
import os, random

def euc_to_clusters(x,y):
    return np.sqrt(np.sum((x-y)**2, axis=1))

class MRKMeans(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRKMeans, self).__init__(*args, **kwargs)
        self.centers_ = pd.read_csv("/tmp/centers.csv",header=None,sep="   ")
        
    def mapper(self, key, line):
        point = np.array(map(np.float,line.split('   ')))
        c = np.argmin(euc_to_clusters(np.array(self.centers_), point))
        yield(c, point)
                        
    def reducer(self, key, tokens):
        def sc(x):
            if len(x) == 1: return "0" + x
            return x
        new_centers = {}
        for val in tokens:
            if new_centers.get(key) == None:
                new_centers[key] = val
            else:
                new_centers[key] = (new_centers[key] + val) / 2. 
        for k in new_centers.keys():
            yield(sc(str(k)),str(new_centers[k]))
        
    def reduce_2(self, key, values):
        for val in values:
            print "---", val

    def steps(self):
        return [self.mr(mapper=self.mapper,reducer=self.reducer),
                self.mr(reducer=self.reduce_2)  ]
if __name__ == '__main__':
    MRKMeans.run()
