import matplotlib.pyplot as plt
from pylab import mpl
import math

"""
牛顿插值法插值的函数表为
xi      0.4，       0.55，     0.65，      0.80，       0.90，   1.05
f(xi)   0.41075,    0.57815,   0.69675,    0.88811,    1.02652,  1.25382
"""

x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]

"""计算五次差商的值"""
def five_order_difference_quotient(x, y):
    # i记录计算差商的次数，这里循环5次，计算5次差商。
    i = 0
    quotient = [0, 0, 0, 0, 0, 0]
    while i < 5:
        j = 5
        while j > i:
            if i == 0:
                quotient[j] = ((y[j] - y[j - 1]) / (x[j] - x[j - 1]))
            else:
                quotient[j] = (quotient[j] - quotient[j - 1]) / (x[j] - x[j - 1 - i])
            j -= 1
        i += 1
    return quotient

def function(data):
    return x[0] + parameters[1] * (data - 0.4) + parameters[2] * (data - 0.4) * (data - 0.55) + parameters[3] * (data - 0.4) * (data - 0.55) * (data - 0.65) + parameters[4] * (data - 0.4) * (data - 0.55) * (data - 0.80)

"""计算插值多项式的值和相应的误差"""
def calculate_data(x, parameters):
    returnData = [];
    for data in x:
        returnData.append(function(data))
    return returnData

"""
画函数的图像
newData为曲线拟合后的曲线
"""
def draw(newData):
    plt.scatter(x, y, label="离散数据", color="red")
    plt.plot(x, newData, label="牛顿插值拟合曲线", color="black")
    plt.scatter(0.596, function(0.596), label="预测函数点", color="blue")
    plt.title("牛顿插值法")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc="upper left")
    plt.show()

parameters = five_order_difference_quotient(x, y)
yuanzu = calculate_data(x, parameters)
draw(yuanzu)
