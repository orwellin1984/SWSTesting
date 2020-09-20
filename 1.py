from matplotlib import pyplot as plt
def func(x):
    y = -0.0008 * x ** 2 + 0.2411 * x + 3.3234
    return y


a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
y2 = []
for i in a:
    b = func(i)
    y2.append(b)

plt.plot(a, y2)
plt.show()
