import numpy as np
import scipy.linalg as lin

DB = lin.toeplitz([1, -1, 0], [1, 0, 0])
print DB; print lin.inv(DB)

DF = lin.toeplitz([-1, 0, 0], [-1, 1, 0])

D_0 = (DF + DB) / 2
print D_0

