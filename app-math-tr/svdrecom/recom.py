import pandas as pd
import numpy.linalg as lin
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv("/home/burak/Downloads/movielens1.csv",sep=';')
import scipy.sparse as sps
df = df.fillna(0)
dfs = sps.coo_matrix(np.array(df.ix[:,1:]))

import scipy.linalg as lin
import scipy.sparse.linalg as slin
U,S,V=slin.svds(dfs,k=7)

plot(U[:,0], U[:,1],'.')

plt.show()

