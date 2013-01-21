from pandas import *
import numpy as np
import numpy.linalg as lin
nyt = read_csv ("nytimes.csv")
nyt = nyt.drop(["class.labels"],axis=1)
nyt = nyt - nyt.mean(0)
nyt2 = nyt.div(nyt.sum(1), axis=0)
nyt2.to_csv("/home/burak/nytimes3.csv")
