'''
Read context of input file, run Cholesky on the contents
output the result in another file
'''
import numpy as np, sys, itertools
from scipy import sparse
import random, re, sys, proj
import numpy.linalg as lin

arr = []
fin = open("/home/burak/Downloads/sasha/node1/BT_sorted.dat")
for x in fin.readlines():
    [id,row] = x.strip().split('\t')
    arr.append(map(np.float,row.split(';')))
    
arr = np.array(arr)

np.savetxt("/tmp/t.txt",arr, fmt='%10.2f', delimiter=';')
arr2 = np.loadtxt("/tmp/t.txt",delimiter=';')

mult = np.dot(arr2.T,arr2)

print mult

print lin.cholesky(mult)

