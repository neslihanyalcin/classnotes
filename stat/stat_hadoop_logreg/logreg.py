'''
Logistic regression for map/reduce written for MRJob. 
'''
from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
import numpy as np
import os, thread

class MRLogisticRegression(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    def __init__(self, *args, **kwargs):
        super(MRLogisticRegression, self).__init__(*args, **kwargs)
        self.n  = 1
        self.m = 3
        self.theta = 2 * np.ones((self.m,1))

    def sigmoid(self, arr):
        return 1.0/(1+np.exp(-arr))

    def stoc_grad_ascent0(self, data_mat, label, theta):
        alpha = 0.002
        for j in range(self.m):
            h = self.sigmoid(np.dot(data_mat,theta)[0])
            theta[j] = theta[j] + alpha * data_mat[j] * (label - h)
        return theta
        
    def mapper(self, key, line):        
        tokens = map(np.float,line.split('\t'))
        data = np.append(1.0,np.array(tokens[:-1]))
        label = np.array(tokens[-1])
        self.theta = self.stoc_grad_ascent0(data, label, self.theta)
        
    def mapper_final(self):        
        yield ("key1", self.theta)
                
    def reducer(self, key, tokens):
        theta = None
        for val in tokens:
            if theta != None: theta = (theta + val) / 2.
            else: theta = val.copy()
        yield('result',str(theta))
        
if __name__ == '__main__':
    MRLogisticRegression.run()
    
