import pygal
'''这个是叠加柱状图'''
# 这里填纵坐标数据，可以填年份之类的
x_data = []
# 这里是具体的指标数据
y_data = []
y_data2 = []
# 创建pygal.StackedBar对象（叠加柱状图）
stacked_bar = pygal.StackedBar()
# 添加两组数据，还有数据标题
stacked_bar.add('', y_data)
stacked_bar.add('', y_data2)
# 设置X轴的刻度值
stacked_bar.x_labels = x_data
# 设置Y轴的刻度值
stacked_bar.y_labels = []
# 设置大标题
stacked_bar.title = ''
# 设置X、Y轴的标题
stacked_bar.x_title = ''
stacked_bar.y_title = ''
# 设置将图例放在底部
stacked_bar.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
stacked_bar.render_to_file('fk_books.svg')