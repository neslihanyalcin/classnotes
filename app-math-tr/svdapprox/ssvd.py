from numpy.linalg import linalg as la
from pandas import *
import numpy as np

def ssvd(df_train):
    # user biases for all movies, that is for all movies all together
    # as a single number per user
    mu = 0.1
    m,n = df_train.shape
    b_u = np.ones((1, m)) * 0.1; b_i = np.ones((1, n)) * 0.1
    p_u = np.ones((1, m)) * 0.1; q_i = np.ones((1, n)) * 0.1
    r_ui = np.zeros((df_train.shape))
    #print b_u.shape, p_u.shape    
    for u in df_train.index:
        print "user", u
        for i,val in enumerate(df_train.ix[u]):
            print "i", i,val
        break
    
if __name__ == "__main__": 

    d =  np.array(
         [[5, 5, np.nan, 5],
         [5, np.nan, 3, 4],
         [3, 4, np.nan, 3],
         [0, np.nan, 5, 3],
         [5, 4, 4, 5],
         [5, 4, 5, 5]])

    data = DataFrame (d.T,
        columns=['S1','S2','S3','S4','S5','S6'],
        index=['Ben','Tom','John','Fred'])

    ssvd(data)
    
