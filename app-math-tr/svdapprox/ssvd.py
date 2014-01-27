from numpy.linalg import linalg as la
import scipy.sparse as sps, itertools
from pandas import *
import numpy as np
import pandas as pd, os

def ssvd(df_train):
    gamma = 0.005 # regularization
    lam = 0.02
    mu = 0.1
    m,n = df_train.shape
    print m,n
    k = 3 # rank
    c = 0.1
    b_u = np.ones(m) * c
    b_i = np.ones(n) * c
    p_u = np.ones((m, k)) * c
    q_i = np.ones((k, n)) * c
    r_ui = np.array(df_train)
    for u in range(m):
        print "user", u
        row = df_train.ix[u]; idxs = row.index[row.notnull()]
        for i in idxs:
            i = int(i)
            r_ui_hat = mu + b_i[i] + b_u[u] + np.dot(q_i[:,i].T,p_u[u,:])
            e_ui = np.nan_to_num(r_ui[u,i]) - r_ui_hat
            b_u[u] = b_u[u] + gamma * (e_ui - lam*b_u[u])
            b_i[i] = b_i[i] + gamma * (e_ui - lam*b_i[i])
            q_i[:,i] = q_i[:,i] + gamma * (e_ui*p_u[u,:].T - lam*q_i[:,i])
            p_u[u,:] = p_u[u,:] + gamma * (e_ui*q_i[:,i].T - lam*p_u[u,:])

    return b_u,b_i,q_i,p_u
            
if __name__ == "__main__": 

    d =  np.array(
         [[5, 5, np.nan, 5],
          [5, np.nan, 3, 4],
          [3, 4, np.nan, 3],
          [np.nan, np.nan, 5, 3],
          [5, 4, 4, 5],
          [5, 4, 5, 5]])

    data = DataFrame (d.T,
        columns=['0','1','2','3','4','5'],
        index=['Ben','Tom','John','Fred'])
    b_u,b_i,q_i,p_u = ssvd(data)
    print b_u
    print b_i
    print q_i
    print p_u

    df = pd.read_csv("%s/Downloads/movielens.csv" % os.environ['HOME'] ,sep=';')
    print df.shape
    df = df.ix[:,1:3700] # id kolonunu atla,
    df.columns = range(3699)
    print df.shape
    df_train = df.ix[:5000,:]
    df_test = df.ix[5001:,:]

    b_u,b_i,q_i,p_u = ssvd(df_train)
    print b_u[10]
    
    
