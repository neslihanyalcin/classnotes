from sasha import job
import numpy as np, sys, itertools
from scipy import sparse
import random, re, sys, proj
import numpy.linalg as lin

arr = []
fin = open(sys.argv[1])
for x in fin.readlines():
    [id,row] = x.strip().split('\t')
    arr.append(map(np.float,row.split(';')))
    
res =  np.array(arr)
print res.shape; print res
print lin.det(res)
print lin.cholesky(res)
    
