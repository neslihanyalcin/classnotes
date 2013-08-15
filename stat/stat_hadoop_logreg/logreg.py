from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
import numpy as np

def sigmoid(arr):
    return 1.0/(1+np.exp(-arr))

def stoc_grad_ascent0(data_mat, label, theta):
    n  = 1
    m = len(data_mat)
    alpha = 0.001
    for j in range(m):
        h = sigmoid(np.dot(data_mat,theta)[0])
        theta[j] = theta[j] + alpha * data_mat[j] * (label - h)
    return theta

class MRLogisticRegression(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    def __init__(self, *args, **kwargs):
        super(MRLogisticRegression, self).__init__(*args, **kwargs)
        #self.theta = np.ones((3,1))
        self.theta = np.array([[1.96503066,-0.11019418,-0.04416265]]).T
        
    def mapper(self, key, line):        
        tokens = map(np.float,line.split('\t'))
        data = np.append(1.0,np.array(tokens[:-1]))
        label = np.array(tokens[-1])
        theta = stoc_grad_ascent0(data, label, self.theta)
        yield ('key1', theta)
                
    def reducer(self, key, tokens):
        theta = None
        for val in tokens:
            if theta != None: theta = (theta + val) / 2.
            else: theta = val.copy()
        yield('result',str(theta))

if __name__ == '__main__':
    MRLogisticRegression.run()
    
