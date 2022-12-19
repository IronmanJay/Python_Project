# 导入第三方模块
import numpy as np
import matplotlib.pyplot as plt
'''这个也是多个数据对比的雷达图'''
# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
# 构造数据
values = [3.2,2.1,3.5,2.8,3]
values2 = [4,4.1,4.5,4,4.1]
feature = ['创新课程和讲座', '创新创业大赛', '创业模拟与实训','创业社团', '创业孵化项目']

N = len(values)
# 设置雷达图的角度，用于平分切开一个圆面
angles=np.linspace(0, 2*np.pi, N, endpoint=False)
# 为了使雷达图一圈封闭起来，需要下面的步骤
values=np.concatenate((values,[values[0]]))
values2=np.concatenate((values2,[values2[0]]))
angles=np.concatenate((angles,[angles[0]]))
# 绘图
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, 'o-', linewidth=2, label = '专科')
# 填充颜色
ax.fill(angles, values, alpha=0.25)
# 绘制第二条折线图
ax.plot(angles, values2, 'o-', linewidth=2, label = '本科')
ax.fill(angles, values2, alpha=0.25)
# 添加每个特征的标签
ax.set_thetagrids(angles * 180/np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0,5)
# 添加标题
plt.title('2018届毕业生对创业服务的评价')
# 添加网格线
ax.grid(True)
# 设置图例
plt.legend(loc = 'best')
# 显示图形
plt.show()









