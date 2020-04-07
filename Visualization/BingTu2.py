import pygal
'''这个是全饼图'''
# 写入数据
data = [2365,5414]
# 写入数据对应的标签，如果想在饼图上显示具体数值，在对应的标签后填入相应数值
labels = ['男生','女生']
# 创建pygal.Pie对象（饼图）
pie = pygal.Pie()
# 采用循环为饼图添加数据
for i, per in enumerate(data):
    pie.add(labels[i], per)
# 标题
pie.title = '男女比例'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 设置内圈的半径长度
pie.inner_radius = 0.4
# 指定将数据图输出到SVG文件中
pie.render_to_file('language_percent.svg')