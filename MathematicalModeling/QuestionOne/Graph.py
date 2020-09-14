import matplotlib.pyplot as plt

# 显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# X轴数据
x_1 = [15,16,17,18,19,20,21,22,23,24,25,26,27,28]
x_2 = [15,16,17,18,19,20,21,22,23,24,25,26,27,28]
# Y轴数据

y_1 = [516,624,732,819,906,1014,1101,1251,1359,1446,1533,1641,1749,1857]
y_2 = [216,366,516,624, 732,819, 906, 1014, 1101, 1251, 1359, 1446, 1533, 1641]
# 设置参数
plt.plot(x_1, y_1, 'ro-', color='#4169E1',linewidth=1, label='第一种情况')
plt.plot(x_2, y_2, 'ro-', color='#e16941',linewidth=1, label='第二种情况')
# 设置标签
plt.legend(loc="upper left")
plt.xlabel('时间/天')
plt.ylabel('背包容量/Kg')

plt.show()
