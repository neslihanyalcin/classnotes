from pandas import *
import numpy as np
import scipy.linalg as linalg

nyt = read_csv ("nytimes.csv")
nyt2 = nyt.ix[:,2:].as_matrix()
means = np.mean(nyt2, axis=0)
meanless_nyt = nyt2 - means
cov_nyt = np.cov(meanless_nyt,rowvar=0)
eigs,eigv = linalg.eig(cov_nyt)
#eig_ind = argsort(eigs)
