import numpy as np
import scipy.linalg as lin

D = lin.toeplitz([1, -1, 0, 0], [1, 0, 0, 0])
print D
