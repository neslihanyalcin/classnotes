from pandas import *
import numpy as np

def scale_cols(df,s):
    return df.apply(lambda x: x*s)

def idf(f):
    print f.shape
    freq = f.astype(bool).sum(axis=0)
    freq = freq.replace(0,1)
    w = np.log(float(f.shape[0])/freq)
    return w

f = read_csv("test.csv")
print idf(f)
print scale_cols(f,np.array([2,2,2,2]))
