import numpy as np
import matplotlib.pyplot as plt


def func(k):
    r = -0.0005378370091112569 * k * k + 0.1729570593267702 * k + 2.2516447428263446
    return r


theta = (np.array(range(0, 370, 5)) * np.pi / 180)
x = [func(i * 100 / np.pi) * np.cos(i) for i in theta]
x1 = [func(i * 100 / np.pi) * np.cos(i + np.pi * 0.5) for i in theta]
x2 = [func(i * 100 / np.pi) * np.cos(i + np.pi) for i in theta]
x3 = [func(i * 100 / np.pi) * np.cos(i + np.pi * 1.5) for i in theta]
y = [func(i * 100 / np.pi) * np.sin(i) for i in theta]
y1 = [func(i*100/np.pi) * np.sin(i + np.pi * 0.5) for i in theta]
y2 = [func(i*100/np.pi) * np.sin(i + np.pi) for i in theta]
y3 = [func(i*100/np.pi) * np.sin(i + np.pi * 1.5) for i in theta]
z = [100 / np.pi * i for i in theta]
ax = plt.figure().add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.plot(x1, y1, z)
ax.plot(x2, y2, z)
ax.plot(x3, y3, z)
plt.show()
