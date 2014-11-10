from scipy.io import mmread, mmwrite
import numpy as np, time, sys
from numba import jit
import os

user_pseudo_average_ratings = np.loadtxt("/tmp/user_pseudo_average_ratings1.dat")
movie_pseudo_average_ratings = np.loadtxt("/tmp/movie_pseudo_average_ratings1.dat")
user_feature_matrix = np.loadtxt("/tmp/user_feature_matrix1.dat")
movie_feature_matrix = np.loadtxt("/tmp/movie_feature_matrix1.dat")
