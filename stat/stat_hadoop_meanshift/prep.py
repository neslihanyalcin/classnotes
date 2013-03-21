#!/usr/bin/python
import os,sys,itertools
import numpy as np
from numpy import linalg as la
os.environ['MPLCONFIGDIR']='/tmp' 
import pandas as pd

comb = lambda x: str(x[0])+":"+str(x[1])
df = pd.read_csv("synthetic.txt",header=None,sep="   ")
df['coord'] = df.apply(comb,axis=1)
df['members'] = ''
df.to_csv("synthetic2.txt",header=None,index=True,cols=['coord','members'],sep='\t')
