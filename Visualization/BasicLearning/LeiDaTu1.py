import numpy as np
import matplotlib.pyplot as plt
'''这个是雷达图'''
# 显示中文
plt.rcParams['font.sans-serif'] = ['KaiTi']
# 标签
labels = np.array([u'就业手续办理(96.74%)', u'学校发布的招聘信息(96.88%)', u'校园招聘会(96.43%)',u'生涯规划(97.16%)','职业咨询与辅导(99.46%)','就业帮扶与推荐(98.84%)'])
# 数据长度
dataLenth = 6
# 数据
data_radar = np.array([96.74, 96.88, 96.43, 97.16,99.46,98.84])
# 分割圆周长
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
# 闭合
data_radar = np.concatenate((data_radar, [data_radar[0]]))
# 闭合
angles = np.concatenate((angles, [angles[0]]))
plt.polar(angles, data_radar, 'bo-', linewidth=1)
# 做极坐标系
plt.thetagrids(angles * 180/np.pi, labels)
# 做标签
plt.fill(angles, data_radar, facecolor='r', alpha=0.25)
# 填充
plt.ylim(0, 100)
# 标题
plt.title(u'2018届毕业生对就业服务的评价')
plt.show()