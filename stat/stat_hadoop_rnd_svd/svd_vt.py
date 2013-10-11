import numpy as np, sys
import numpy.random as rand
import numpy.linalg as lin
import matplotlib.pyplot as plt
import pandas as pd

x,x,VT = lin.svd(np.loadtxt(sys.argv[1],delimiter=';'))
np.savetxt(sys.argv[2],VT,delimiter=';')
