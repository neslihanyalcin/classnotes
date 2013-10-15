from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol
from mrjob.protocol import RawValueProtocol
from mrjob.protocol import RawProtocol
import numpy as np, sys, itertools
from scipy import sparse

def line_to_coo(line, dim):
    line = line.replace('"','')
    tokens = line.split(";")
    line_sps = sparse.lil_matrix((1,dim))
    for tok in tokens:
        tmp = tok.split(":"); line_sps[ 0,int(tmp[0]) ] = float(tmp[1])
    return line_sps.tocoo()
    
