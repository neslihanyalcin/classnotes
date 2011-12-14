import numpy as np

patents = np.array([  4.,   3.,   2.,   8.,   4.,  
                      4.,  10.,   4.,  10.,   7.])

def u(n,k):
    if n-k < 0: return 0
    return 1.

def y(n,data):
    sum = 0
    for k in range(len(data)):
        sum += data[k]*(0.85**(n-k))*u(n,k)
    return sum
        
for n in range(len(patents)):    
    print  y(n,patents)
    
