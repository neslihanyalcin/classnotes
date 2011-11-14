import numpy as np
import scipy.linalg
A = [[2,3,4],[5,5,6],[7,7,7]]
b = [1,2,3]
u = scipy.linalg.solve(A, b)
print u
c = [2,3,8]
bc = np.vstack((b,c)).T
u = scipy.linalg.solve(A,  bc)
print u
