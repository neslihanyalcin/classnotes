from pandas import *
import numpy as np
import numpy.linalg as lin
nyt = read_csv ("nytimes.csv")
nyt = nyt.drop(["class.labels"],axis=1)
nyt = nyt - nyt.mean(0)
nytn = nyt.div(nyt.sum(1), axis=0)
#u,s,v = lin.svd(nytn)
