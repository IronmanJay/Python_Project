import pygal
'''这个是点图'''
# x轴数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500,58300, 56800, 59500, 62700]
# 创建pygal.Dot对象（点图）
dot = pygal.Dot()
dot.dots_size = 5
# 添加两组数据
dot.add('本科', y_data)
dot.add('专科', y_data2)
# 设置X轴的刻度值
dot.x_labels = x_data
# 重新设置Y轴的刻度值
dot.y_labels = ['本科', '专科']
# 设置Y轴刻度值的旋转角度
dot.y_label_rotation = 45
dot.title = '历年学校毕业生就业情况'
# 设置X轴的标题
dot.x_title = '年份'
# 设置将图例放在底部
dot.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
dot.render_to_file('fk_books.svg')