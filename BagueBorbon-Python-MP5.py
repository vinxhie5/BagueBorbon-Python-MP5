# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pylab as plt

n = np.arange(0,200)

def x(n):
    s = eval(z)
    return s

z = (input('Enter a value for x(n): '))
for k in range(0,200):
    if k == 0:
        y = (-1.5*x(n)) + (2*x(n+1)) - (0.5*x(n+2))
        
    elif k>0 and k<=198:
        y = (0.5*x(n+1)) - (0.5*x(n-1))
        
    else:
        y = (1.5*x(n)) - (2*x(n-1)) + (0.5*x(n-2))

plt.plot(x(n), color = 'b', label = 'y(n)')
plt.plot(y, color = 'g', label = 'x(n)')
plt.grid()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show

    