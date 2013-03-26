#!/usr/bin/python
import pandas as pd
import os,sys,itertools
import numpy as np
os.environ['MPLCONFIGDIR']='/tmp' 
from sklearn.neighbors import NearestNeighbors

def coords(x): # splits 2d coordinates seperated by colon
    return pd.Series(np.array(str(x).split(":"),dtype=np.float64))

bandwidth = 2000
stop_thresh = 1e-3 * bandwidth 

df = pd.read_csv(sys.stdin,na_values='',header=None,
                 names=['window','center','members'],sep="\t")

centers = np.array(df['center'].apply(coords))
nbrs = NearestNeighbors(radius=bandwidth).fit(centers)
print len(centers)
visited = np.array([])
for my_mean in centers:
    print my_mean
    i_nbrs = nbrs.radius_neighbors([my_mean],
                                   bandwidth, return_distance=False)[0]
    centers_within = centers[i_nbrs]
    print "centers_within", centers_within
    print "visited",visited
    centers_within = centers_within[centers_within != visited]
    print "centers_within not visited", centers_within
    visited=np.hstack((i_nbrs,visited))
    #break
