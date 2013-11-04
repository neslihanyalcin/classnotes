from mrjob.job import MRJob
import numpy as np, sys, itertools
import scipy.sparse as sps, re

def key_val_to_coo(line, dim):
    line_sps = sps.lil_matrix((1,dim))
    ids = re.findall("(\d+):(\d+)",line)
    def f(x): line_sps[0,long(x[0])] = np.float(x[1])
    map(f, ids)
    return line_sps.tocoo()
    
