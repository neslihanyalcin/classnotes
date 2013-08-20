from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
import numpy as np, sys
import pandas as pd
import os, random, ast

def euc_to_clusters(x,y):
    return np.sqrt(np.sum((x-y)**2, axis=1))

class MRKMeans(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    
    def __init__(self, *args, **kwargs):
        super(MRKMeans, self).__init__(*args, **kwargs)
        self.centers_ = pd.read_csv("/tmp/centers.csv",header=None,sep="   ")
        self.k = 15
        self.new_centers = np.zeros((self.k,2))
        self.counts = np.zeros((self.k,))
        
    def mapper(self, key, line):
        point = np.array(map(np.float,line.split('   ')))
        c = np.argmin(euc_to_clusters(np.array(self.centers_), point))
        yield(c, point)
                        
    def reducer(self, key, tokens):
        for val in tokens:
            self.new_centers[key] += val
            self.counts[key] += 1
        yield('final', self.new_centers[key] / self.counts[key])
        
    def reduce_all_centers(self, key, values):
        self.f=open("/tmp/centers.csv","w")
        for val in values:
            self.f.write("   ".join(map(str,val)))
            self.f.write("\n")
        self.f.close()
        
    def steps(self):
        return [self.mr(mapper=self.mapper,reducer=self.reducer),
                self.mr(reducer=self.reduce_all_centers)]
    
if __name__ == '__main__':
    for i in range(10): MRKMeans.run()
