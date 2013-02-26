#!/usr/bin/python
import os,sys
from numpy import linalg as la

def euclid(inA,inB):
    return la.norm(inA - inB)

os.environ['MPLCONFIGDIR']='/tmp' 
import pandas as pd
df = pd.read_csv(sys.stdin,names=['a','b'],sep="   ")
centers = pd.read_csv("/tmp/centers.csv",sep=",")
