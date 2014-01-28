from numpy.linalg import linalg as la
import scipy.sparse as sps, itertools
import numpy as np
import random
import pandas as pd, os

def create_training_test(df):
    test_data = []
    df_train = df.copy()
    for u in range(df.shape[0]):
        row = df.ix[u]; idxs = row.index[row.notnull()]
        i = random.choice(idxs); val = df.ix[u,i]
        test_data.append([u,i,val])
        df_train.ix[u,i] = np.nan
    return df_train, test_data

def ssvd(df_train,rank):
    print rank
    gamma = 0.02 # regularization
    lam = 0.2
    
    mu = df_train.mean().mean()
    m,n = df_train.shape
    print m,n
    c = 0.08
    b_u = np.ones(m) * c
    b_i = np.ones(n) * c
    p_u = np.ones((m, rank)) * c
    q_i = np.ones((rank, n)) * c
    r_ui = np.array(df_train)
    for u in range(m):
        #print "user", u
        row = df_train.ix[u]; idxs = row.index[row.notnull()]
        for i in idxs:
            i = int(i)
            r_ui_hat = mu + b_i[i] + b_u[u] + np.dot(q_i[:,i].T,p_u[u,:])
            e_ui = r_ui[u,i] - r_ui_hat
            b_u[u] = b_u[u] + gamma * (e_ui - lam*b_u[u])
            b_i[i] = b_i[i] + gamma * (e_ui - lam*b_i[i])
            q_i[:,i] = q_i[:,i] + gamma * (e_ui*p_u[u,:].T - lam*q_i[:,i])
            p_u[u,:] = p_u[u,:] + gamma * (e_ui*q_i[:,i].T - lam*p_u[u,:])
    return mu,b_u,b_i,q_i,p_u
            
