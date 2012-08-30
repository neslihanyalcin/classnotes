import matplotlib.pyplot as plt
import itertools
import numpy as np

Img = plt.imread("twoObj.jpg")
n = Img.shape[0]
Img2 = Img.flatten(order='C')
nn = Img2.shape[0]

A = np.zeros((nn,nn))

for i in range(nn):
    for j in range(nn):
        A[i,j]=np.exp(-((Img2[i]-Img2[j])**2))
        
V,D = np.linalg.eig(A)
V = np.real(V)
a = np.real(D[0])
print a

threshold = 0 # filter
a = np.reshape(a, (n,n))
Img[a<threshold] = 255
plt.imshow(Img)
plt.show()

