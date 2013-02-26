#!/usr/bin/python
import os,sys
os.environ['MPLCONFIGDIR']='/tmp' 
import pandas as pd
df = read_csv(sys.stdin,names=['a','b'],sep="   ")
centers = read_csv("centers.csv",sep=",")
