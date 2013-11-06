import pandas as pd
import numpy.linalg as lin
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import numpy.linalg as lin
df = pd.read_csv("/home/burak/Downloads/movielens1.csv",sep=';')
print 'loaded'
U,S,VT = lin.svd(np.array(df.ix[:,1:]))
print 'svd'
plt.plot(U[:,0], U[:,1],'.')
plt.show()

