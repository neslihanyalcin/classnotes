# UNDER DEVELOPMENT
# HALA GELISTIRILIYOR

import matplotlib.pyplot as plt
import numpy as np

def n_max(arr, n):
    indices = arr.ravel().argsort()[-n:]
    indices = (np.unravel_index(i, arr.shape) for i in indices)
    return [(arr[i], i) for i in indices]

Img = plt.imread("twoObj.jpg")
(n,dummy) = Img.shape
Img2 = Img.flatten()
(nn,) = Img2.shape

A = np.zeros((nn,nn))

for i in range(nn):
    for j in range(nn):
        N=Img2[i]-Img2[j];
        A[i,j]=np.exp(-(N**2))

V,D = np.linalg.eig(A)
V = np.real(V)
res = n_max(V,1) # take largest 
idx = res[0][1][0] 
a = np.real(D[idx]) # look at corresp eigv

threshold = 1e-20 # filter
a[a<threshold] = 0
a[a>0] = 1
print a

a = np.reshape(a, (n,n))
Img[a==1] = 255
plt.imshow(Img)
plt.show()
