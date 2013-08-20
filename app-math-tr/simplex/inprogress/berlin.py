import numpy as np
import simplex

A = np.array([[1, 1],[16, 8],[9000, 5000] ])
b = np.array([[44],[512],[300000]]);
basis = np.array([2]);
c = np.array([30000, 20000]);
x,y,cost = simplex.simplex(A,b,c,basis)
print x
print y
print cost
