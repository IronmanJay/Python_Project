from pyecharts import Bar
'''柱状图'''
# 输入横坐标数据
attr=["机械","曙光","人艺","冶金","管理","外语"]
# 输入纵坐标数据（一）
v1=[5,20,36,10,75,90]
# 输入纵坐标数据（二）
v2=[10,25,8,60,20,80]
# 设置标题
bar=Bar("2017-2018年度各院优秀学生人数")
# 设置副标题（一）
bar.add("2017年",attr,v1,is_stack=True)
# 设置副标题（二）
bar.add("2018年",attr,v2,is_stack=True)
# 生成html，打开即可
bar.render()
