from matplotlib import pyplot as plt
import numpy as np
import math


def func(x):
    y = -0.00075 * x ** 2 + 0.2409 * x + 3.3234
    return y


a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
b = [4.7, 8.3, 11.3, 14.2, 16.8, 19.3, 21.6, 23.15, 24.7, 26.4, 28.0, 29.1, 30.1, 31.1, 32.0, 32.55, 32.2]
na = np.array(a)
nb = np.array(b)
y2 = []
for i in a:
    b = func(i)
    y2.append(b/2)

bl = (nb / math.sqrt(2))/2
print(bl)
print(np.array(y2))
plt.plot(na, bl, '-o')
plt.plot(a, y2)
plt.xlim(0)
plt.ylim(0)
plt.grid(linestyle='-.')
plt.show()
"""
plt.plot(na, nb, '-o')
plt.xlim(0)
plt.ylim(0)
plt.show()
"""
