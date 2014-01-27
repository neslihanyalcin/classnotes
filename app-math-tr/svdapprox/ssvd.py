from numpy.linalg import linalg as la
from pandas import *
import numpy as np

def ssvd(df_train):
    gamma = 0.005 # regularization
    lam = 0.02
    mu = 0.1
    m,n = df_train.shape
    print m,n
    k = 3 # rank
    b_u = np.ones((1, m)) * 0.1
    b_i = np.ones((1, n)) * 0.1
    p_u = np.ones((m, k)) * 0.1
    q_i = np.ones((k, n)) * 0.1
    r_ui = np.array(df_train).copy()
    r_ui[:] = np.nan
    for u in range(m):
        print "user", u        
        for i in range(n):
            print "i", i
            print p_u[u,:].shape
            print q_i[:,i].shape
            r_ui_hat = mu + b_i[0,i] + b_u[0,u] + np.dot(q_i[:,i].T,p_u[u,:])
            e = np.nan_to_num(r_ui[u,i]) - r_ui_hat
            print e
        break
    
if __name__ == "__main__": 

    d =  np.array(
         [[5, 5, np.nan, 5],
          [5, np.nan, 3, 4],
          [3, 4, np.nan, 3],
          [np.nan, np.nan, 5, 3],
          [5, 4, 4, 5],
          [5, 4, 5, 5]])

    data = DataFrame (d.T,
        columns=['S1','S2','S3','S4','S5','S6'],
        index=['Ben','Tom','John','Fred'])

    ssvd(data)
    
