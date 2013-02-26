#!/usr/bin/python
import os,sys,itertools
import numpy as np
from numpy import linalg as la
os.environ['MPLCONFIGDIR']='/tmp' 
import pandas as pd

centers = pd.read_csv("/tmp/centers.csv",header=None,sep=",")
print centers[:4]

def dist(vect,x):
    return np.fromiter(itertools.imap(np.linalg.norm, vect-x),dtype=np.float)

def closest(x):
    d = dist(np.array(centers)[:,1:3],np.array(x))
    return np.argmin(d)

df = pd.read_csv(sys.stdin,header=None,sep="   ")
df['closest'] = df.apply(closest,axis=1)
print df[:20]
