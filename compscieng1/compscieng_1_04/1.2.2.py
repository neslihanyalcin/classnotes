import numpy as np
import numpy.linalg as lin
import ktbc

K,T,B,C = ktbc.ktbc(4)

print lin.inv(K) 
