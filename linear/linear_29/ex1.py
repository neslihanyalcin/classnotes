import scipy.linalg as lin
import numpy as np

print '\nA.T*A\n'
a = np.array([[4,4],[-3,3]])
print np.dot(a.T,a)

print '\nEig of A.T*A\n'
a = np.array([[25,7],[7,25]])
w,vl =  lin.eig(a)
print w
print vl

print '\nEig of A*A.T\n'
a = np.array([[32,0],[0,18]])
w,vl =  lin.eig(a)
print w
print vl

print '\nVerify\n'
a1 = np.array([[1,0],[0,1]])
a2 = np.array([[np.sqrt(32),0],[0,np.sqrt(18)]])
a3 = np.array([[1./np.sqrt(2),1./np.sqrt(2)],
               [1./np.sqrt(2),-1./np.sqrt(2)]])

print np.dot(a1,np.dot(a2,a3))

print '\nReal SVD\n'

a = np.array([[4,-3],[4,3]])
U,s,Vh =  lin.svd(a)

print U
print s
print Vh

