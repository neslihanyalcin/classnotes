#
# MIT OCW ODE Mathlet Complex Exponentials replacement in 
# Python
#
from pylab import *
from matplotlib.widgets import Slider

ax = subplot(121)
subplots_adjust(left=0.1, bottom=0.25)
l1, = plot(None,None, lw=2, color='red')
axis([-1, 1, -8, 8])
title ('$(a + bi)t$', color='blue')
grid()

ax = subplot(122)
subplots_adjust(left=0.1, bottom=0.25)
l2, = plot(None,None, lw=2, color='red')
axis([-3, 3, -3, 3])
title ('$e^{(a + bi)t}$', color='blue')
grid()

axcolor = 'lightgoldenrodyellow'
axa = axes([0.15, 0.1, 0.65, 0.03], axisbg=axcolor)
axb  = axes([0.15, 0.15, 0.65, 0.03], axisbg=axcolor)

slidera = Slider(axa, 'a', -1.0, 1.0, valinit=0)
sliderb = Slider(axb, 'b', -8.0, 8.0, valinit=0)

def update(val):
    a = slidera.val
    b = sliderb.val
    t = arange(-1.0, 1.0, 0.001)
    l1.set_xdata(t)
    l1.set_ydata((b/a)*t)

    t = arange(-3.0, 3.0, 0.001)
    l2.set_xdata(exp(a*t)*cos(b*t))
    l2.set_ydata(exp(a*t)*sin(b*t))
    draw()
    
slidera.on_changed(update)
sliderb.on_changed(update)

show()

