import numpy as np
import scipy.linalg
A = [[2,3,4],[5,5,6],[7,7,7]]
b = [1,2,3]
lu = scipy.linalg.lu(A)
qr = scipy.linalg.qr(A)
e = scipy.linalg.eig(A)
svd = scipy.linalg.svd(A)

