import matplotlib.pyplot as plt
from pylab import *  # 支持中文
'''这个是折线图'''
mpl.rcParams['font.sans-serif'] = ['SimHei']
names = ['2011', '2012', '2013', '2014', '2015']
x = range(len(names))
y = [0.81, 0.84, 0.85, 0.86,0.87]
y1 = [0.71, 0.75, 0.79, 0.82, 0.85]
plt.plot(x, y, marker='o', mec='r', mfc='w', label='本科')
plt.plot(x, y1, marker='*', ms=10, label=u'专科')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
# X轴标签
plt.xlabel(u"time(y)年份")
# Y轴标签
plt.ylabel("占比")
# 标题
plt.title("辽科院毕业生就业情况")
plt.show()