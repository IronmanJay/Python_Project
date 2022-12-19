from pyecharts import Line,Pie,Grid
'''这个是组合图'''
# 首先设置折线图
line=Line("折线图",width=1200)
# 设置折线图x轴标签
attr=["周一","周二","周三","周四","周五","周六","周日"]
# 分别设置折线图的两条线
line.add("最高气温",attr,[11,11,15,13,12,13,10],mark_point=["max","min"],mark_line=["average"])
line.add("最低气温",attr,[1,-2,2,5,3,2,0],mark_point=["max","min"],mark_line=["average"],legend_pos="20%")
# 准备饼图的标签
attr=["机械","曙光","人艺","冶金","管理","外语"]
# 准备饼图的数据
v1=[11,12,13,10,10,10]
# 设置饼图
pie=Pie("饼图",title_pos="55%")
# 设置属性
pie.add("",attr,v1,radius=[45,65],center=[65,50],legend_pos="80%",legend_orient="vertical")
grid=Grid()
grid.add(line,grid_right="55%")
grid.add(pie,grid_left="60%")
# 生成html，打开即可
grid.render()