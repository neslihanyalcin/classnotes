import os
from pandas import *
import numpy as np

df = read_csv("synthetic.txt",names=['a','b'],sep="   ")
centers = DataFrame(np.random.randn(10,2)) * np.array(df.mean())
centers.to_csv("/tmp/centers.txt",header=None)
os.system("ssh localhost -l hduser /home/hduser/Downloads/hadoop*/bin/hadoop dfs -copyFromLocal /tmp/centers.txt /user/hduser")
os.system("ssh localhost -l hduser /home/hduser/Downloads/hadoop*/bin/hadoop dfs -cat /user/hduser/centers.txt")
