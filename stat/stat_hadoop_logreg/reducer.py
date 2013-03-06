#!/usr/bin/python
import os,sys,itertools
import numpy as np
from numpy import linalg as la
os.environ['MPLCONFIGDIR']='/tmp' 
import pandas as pd

def new_val(x):
    return pd.Series(np.array(str(x).split(","),dtype=np.float64))

df = pd.read_csv(sys.stdin,sep="\t",names=['key','val'])
df2 = df['val'].apply(new_val)
df3 = df.combine_first(df2)
df4 =  df3.groupby('key').mean()
df4.to_csv(sys.stdout, sep=',',header=None)
