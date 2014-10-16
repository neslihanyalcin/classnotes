import scipy.sparse as sps
import scipy.io as io
import pandas as pd, os, sys, felz
import itertools, numpy as np

syn = pd.read_csv("../kmeans/synthetic.txt",names=['a','b'],sep="   ")
data = np.array(syn)

from sklearn.metrics.pairwise import euclidean_distances
X = euclidean_distances(data, data)

X2 = X.copy()

# filter out large values / distances so matrix can be sparse
X2[X > 2000] = 0.0
X3 = sps.lil_matrix(X2)
X4 = sps.triu(X3)
print 'non-zero items', len(X4.nonzero()[0])
print X4.shape

clf = felz.Felzenswalb(threshold=100,c=60000)
clf.fit(X4)
syn['cluster'] = clf.labels_
print len(syn['cluster'].unique())
