from pyecharts import Pie
'''饼图'''
# 输入标签
attr=["机械","曙光","人艺","冶金","管理","外语"]
# 输入各标签数据
v1=[11,12,13,10,10,10]
# 设置标题
pie=Pie("各院优秀学生人数")
# 设置属性
pie.add("",attr,v1,is_label_show=True)
# 生成html，打开即可
pie.render()