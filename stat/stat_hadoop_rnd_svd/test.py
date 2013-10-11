# Pure Halko
import numpy as np
import numpy.random as rand
import numpy.linalg as lin
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/home/burak/Downloads/movielens1-small.csv",header=None,sep=';')
print len(df.columns)
df = df.drop(0,axis=1)
print len(df.columns)

U, Sigma, V = lin.svd(df);
plt.plot(U[:,0],U[:,1],'bx')

plt.hold(True)

