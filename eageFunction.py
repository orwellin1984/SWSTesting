"""
本程序的主要目的是对测量得到的数据进行最小二乘计算，得到拟合函数，将ScrewPoint的边缘函数化
Version: 0.01
E-mail: orwell.in1984@gmail.com
By: Luning
"""
#!/usr/bin/env python
# coding:utf-8


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

# 待拟合的数据
X = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])
Y = np.array([4.775, 7.60, 10.8, 14.775, 16.45, 18.95, 20.55, 23.5, 25.225, 26.925, 28.325, 29.525,
              30.675, 31.625, 32.425, 32.275, 32.1, 31.8])/2


# 二次函数的标准形式
def func(params, x):
    a, b, c = params
    return a * x * x + b * x + c


# 误差函数，即拟合曲线所求的值与实际值的差
def error(params, x, y):
    return func(params, x) - y


# 对参数求解
def slovePara():
    p0 = [10, 10, 10]

    Para = leastsq(error, p0, args=(X, Y))
    return Para


# 输出最后的结果
def solution():
    Para = slovePara()
    a, b, c = Para[0]
    print("a=", a, " b=", b, " c=", c)
    print("cost:" + str(Para[1]))
    print("求解的曲线是:")
    print("y=" + str(a) + "x*x+" + str(b) + "x+" + str(c))

    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, color="green", label="sample data", linewidth=2)

    #   画拟合直线
    x = np.linspace(0, 180, 550)  # 在0-15直接画100个连续点
    y = a * x * x + b * x + c  # 函数式
    plt.plot(x, y, color="red", label="solution line", linewidth=2)
    plt.legend()  # 绘制图例
    plt.show()


solution()
