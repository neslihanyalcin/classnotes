import numpy as np
import scipy.linalg as lin
import ktbc

K, T, B, C = ktbc.ktbc(3)
print lin.inv(K)
print lin.det(K)
print lin.det(K) * lin.inv(K)

K, T, B, C = ktbc.ktbc(5)
print lin.det(K)
print lin.inv(K)
print lin.det(K) * lin.inv(K)

