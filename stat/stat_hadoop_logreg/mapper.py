#!/usr/bin/python
import os,sys,itertools
import numpy as np
from numpy import linalg as la
os.environ['MPLCONFIGDIR']='/tmp' 
import pandas as pd

def sigmoid(arr):
    return 1.0/(1+np.exp(-arr))

def stoc_grad_ascent0(data_mat, label_mat):
    m,n = data_mat.shape
    label_mat=label_mat.reshape((m,1))
    theta = np.ones((n,1))
    alpha = 0.001
    for i in range(m):
        h = sigmoid(np.sum(np.dot(data_mat[i],theta)))
        error = label_mat[i] - h
        theta = theta + alpha * data_mat[i].reshape((n,1)) * error
    return theta

df = pd.read_csv(sys.stdin,header=None,names=['x','y','labels'],sep='\t')
df['intercept']=1.0
data = df[['intercept','x','y']]
theta = np.array(stoc_grad_ascent0(np.array(data),df['labels']))
print "KEY1\t" + ",".join([str(x) for x in theta[:,0]])
