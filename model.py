
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 6, 8])
y = np.array([660, 160, 72, 42, 20, 10])


def fit_func(x, a, b, c):
    return a/(b*x**2 + c)


def connectpoints(x, y, p1, p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1, x2], [y1, y2], 'k-')


xmin = 1
xmax = 9
params = curve_fit(fit_func, x, y)

[a, b, c] = params[0]
y = []
numpoints = 100

for i in range(numpoints):
    y.append(a/(b*(i/numpoints*(xmax-xmin))**2+c))

x=[]
for i in range(numpoints):
    x.append(i/numpoints*(xmax-xmin))

plt.plot(x, y, 'ro')
for i in range(0,len(x)-1):
    if y[i] >0:
        connectpoints(x, y, i, i+1)

plt.xlim([xmin, xmax])
plt.ylim([0, 600])

plt.show()
