from pylab import *
import numpy as np

data = loadtxt("glass.data",delimiter=",")
head = data[data[:,10]==7]
tableware = data[data[:,10]==6]
containers = data[data[:,10]==5]

print head[:,1]

data =(containers[:,1], tableware[:,1], head[:,1])

yticks([1, 2, 3], ['containers', 'tableware', 'head'])

boxplot(data,0,'rs',0,0.75)

show()
