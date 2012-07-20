import numpy as np
import scipy.linalg as lin
import Levenshtein as leven
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import itertools
import time

words = np.array(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                  'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                  'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we',
                  'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all',
                  'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if',
                  'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make',
                  'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take',
                  'people', 'into', 'year', 'your', 'good', 'some', 'could',
                  'them', 'see', 'other', 'than', 'then', 'now', 'look',
                  'only', 'come', 'its', 'over', 'think', 'also', 'back',
                  'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well',
                  'way', 'even', 'new', 'want', 'because', 'any', 'these',
                  'give', 'day', 'most', 'us'])

print "calculating distances..."

(dim,) = words.shape
f = lambda (x,y): leven.distance(x,y)
res=np.fromiter(itertools.imap(f, itertools.product(words, words)), dtype=float)
A = np.reshape(res,(dim,dim))

print "svd..."

u,s,v = lin.svd(A, full_matrices=False)

print u.shape
print s.shape
print s
print v.shape

k=KMeans(init='k-means++', k=25, n_init=10)
k.fit(u[:,0:10])
centroids = k.cluster_centers_
labels = k.labels_
print labels

for i in range(np.max(labels)):
    print words[labels==i]

plt.plot(centroids[:,0],centroids[:,1],'x')
plt.hold(True)
plt.plot(u[:,0], u[:,1], '.')
plt.show()

