# 导入绘图模块
import matplotlib.pyplot as plt
import numpy as np
'''这个是比较柱状图，可用于一个城市不同年份，一个学校不同年份的比较'''
# 构建两个数据
Y2016 = []
Y2017 = []
# 设置横坐标标签
labels = []
bar_width = 0.45
# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 绘图
plt.bar(np.arange(5), Y2016, label = '2016', color = 'steelblue', alpha = 0.8, width = bar_width)
plt.bar(np.arange(5)+bar_width, Y2017, label = '2017', color = 'indianred', alpha = 0.8, width = bar_width)
# 添加横坐标轴标签
plt.xlabel('')
# 添加纵坐标轴标签
plt.ylabel('')
# 添加标题
plt.title('')
# 添加刻度标签
plt.xticks(np.arange(5)+bar_width,labels)
# 设置纵坐标的刻度范围
plt.ylim([])
# 为每个条形图添加数值标签
for x2016,y2016 in enumerate(Y2016):
    plt.text(x2016, y2016+100, '%s' %y2016)
for x2017,y2017 in enumerate(Y2017):
    plt.text(x2017+bar_width, y2017+100, '%s' %y2017)
# 显示图例
plt.legend()
# 显示图形
plt.show()