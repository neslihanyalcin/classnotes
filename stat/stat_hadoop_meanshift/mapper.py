#!/usr/bin/python
import pandas as pd
import os,sys,itertools
import numpy as np
os.environ['MPLCONFIGDIR']='/tmp' 
from sklearn.neighbors import NearestNeighbors

def coords(x):
    return pd.Series(np.array(str(x).split(":"),dtype=np.float64))

bandwidth = 2000
stop_thresh = 1e-3 * bandwidth 

df = pd.read_csv(sys.stdin,na_values='',header=None,
                 names=['window','center','members'],sep="\t")

X = np.array(df['center'].apply(coords))
nbrs = NearestNeighbors(radius=bandwidth).fit(X)
print len(X)
for my_mean in X:
    print my_mean
    i_nbrs = nbrs.radius_neighbors([my_mean],
                                   bandwidth, return_distance=False)[0]
    points_within = X[i_nbrs]    
    break
