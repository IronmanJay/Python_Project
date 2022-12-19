# 导入绘图模块
import matplotlib.pyplot as plt
'''这个是水平柱状图'''
# 构建数据
price = []
# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 绘图
plt.barh(range(5), price, align = 'center',color='steelblue', alpha = 0.8)
# 添加横坐标标签
plt.xlabel('')
# 添加标题
plt.title('')
# 添加纵坐标标签
plt.yticks(range(5),[])
# 设置横坐标的刻度范围
plt.xlim([])
# 为每个条形图添加数值标签
for x,y in enumerate(price):
    plt.text(y+0.1,x,'%s' %y,va='center')
# 显示图形
plt.show()