# 导入绘图模块
import matplotlib.pyplot as plt
'''这个是标准柱状图'''
# 构建数据
NUM = []
# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 绘图
plt.bar(range(4), NUM, align = 'center',color='steelblue', alpha = 0.8)
# 添加横坐标标签
plt.ylabel('')
# 添加标题
plt.title('')
# 添加刻度标签，横坐标
plt.xticks(range(4),[])
# 设置纵坐标轴的刻度范围
plt.ylim([])
# 为每个条形图添加数值标签
for x,y in enumerate(NUM):
    plt.text(x,y+100,'%s' %round(y,1),ha='center')
# 显示图形
plt.show()