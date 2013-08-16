from pylab import *

xmax = 6.
xmin = -6.
D = 100
x = linspace(xmin, xmax, D)

a = 3
b = 1

plot(x, (a*cos(x) + b*sin(x)))
plot(x, (a*cos(x)))
plot(x, (b*sin(x)))

grid()
legend(['sum', 'cos','sin'])

show()

