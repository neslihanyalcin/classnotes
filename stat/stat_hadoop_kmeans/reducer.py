#!/usr/bin/python
import os,sys,itertools
import numpy as np
from numpy import linalg as la
os.environ['MPLCONFIGDIR']='/tmp' 
import pandas as pd

def coords(x):
    return np.array(str(x).split(":"),dtype=np.float64)

def my_mean(x):
    return pd.Series(np.mean(x['coord_new']),index=['cluster','coord'])

df = pd.read_csv(sys.stdin,sep="\t",names=['cluster','coord'])
df['coord_new'] = df['coord'].apply(coords)
df2 = df.groupby('cluster').apply(my_mean)
df2.to_csv(sys.stdout, sep=',',header=None)
