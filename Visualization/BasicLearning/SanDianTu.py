from pyecharts import Scatter
'''散点图'''
# 输入数据
v1=[10,20,30,40,50,60]
v2=[10,20,30,40,50,60]
# 设置标题
scatter=Scatter("示例")
# 设置标签
scatter.add("A",v1,v2)
scatter.add("B",v1[::-1],v2)
# 生成html，打开即可
scatter.render()