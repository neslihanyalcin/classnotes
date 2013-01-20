from pandas import *
import numpy as np
import numpy.linalg as linalg

nyt = read_csv ("nytimesn.csv")
nyt2 = nyt.ix[:,2:].as_matrix()
#means = np.mean(nyt2, axis=0)
#meanless_nyt = nyt2 - means
cov_nyt = np.cov(nyt2,rowvar=0)
print cov_nyt.shape
eigs,eigv = linalg.eig(cov_nyt)
#eig_ind = argsort(eigs)
