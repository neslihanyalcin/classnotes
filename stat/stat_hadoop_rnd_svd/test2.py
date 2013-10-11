import numpy as np

a = np.array([[3,4,5],[3,5,5],[5,5,9],[9,9,9]])
b = np.array([[8,1],[8,2],[8,3],[8,4]])

print a.shape
print b.shape

print np.dot(a.T,b)
