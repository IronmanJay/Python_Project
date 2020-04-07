# 导入第三方模块
import matplotlib.pyplot as plt
'''这个是分离全饼图'''
plt.style.use('ggplot')

# 写入数据
edu = [0.1524,0.1492,0.1433,0.1111,0.1093,0.1028,0.0932,0.0730]
# 写入数据对应的标签
labels = ['管理学院','电气与信息工程学院','资源与土木工程学院','人文艺术学院','机械工程学院','生物医药与化学工程学院','冶金学院','曙光学院']

explode = [0.1,0,0,0,0,0,0,0]  # 用于突出显示某一个数据
colors=['#9999ff','#ff9999','#7777aa','#2442aa','#dd5555','#7777aa','#ff9999','#ff9999'] # 自定义颜色

# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0,4)
plt.ylim(0,4)

# 绘制饼图
plt.pie(x = edu, # 绘图数据
        explode=explode, # 突出显示某一数据
        labels=labels, # 添加标签
        colors=colors, # 设置饼图的自定义填充色
        autopct='%.1f%%', # 设置百分比的格式，这里保留一位小数
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance = 1.20, # 设置标签与圆心的距离
        startangle = 180, # 设置饼图的初始角度
        radius = 1.5, # 设置饼图的半径
        counterclock = False, # 是否逆时针，这里设置为顺时针方向
        wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},# 设置饼图内外边界的属性值
        textprops = {'fontsize':12, 'color':'k'}, # 设置文本标签的属性值
        center = (1.8,1.8), # 设置饼图的原点
        frame = 1 )# 是否显示饼图的图框，这里设置显示

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('各学院人员分布情况')

# 显示图形
plt.show()