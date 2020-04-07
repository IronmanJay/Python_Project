import pygal
'''这个是多个数据对比的雷达图'''
# 准备数据
data = [[5, 4.0, 5, 5, 5],
    [4.8, 2.8, 4.8, 4.8, 4.9],]
# 准备标签
labels = ['本科','专科']
# 创建pygal.Radar对象（雷达图）
rader = pygal.Radar()
# 采用循环为雷达图添加数据
for i, per in enumerate(labels):
    rader.add(labels[i], data[i])
# 设置标签
rader.x_labels = ['创新课程和讲座', '创新创业大赛', '创业模拟与实训','创业社团', '创业孵化项目']
rader.title = '2018届毕业生对创业服务的评价'
# 控制各数据点的大小
rader.dots_size = 8
# 设置将图例放在底部
rader.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
rader.render_to_file('language_compare.svg')