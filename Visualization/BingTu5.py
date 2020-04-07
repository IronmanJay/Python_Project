from pyecharts import Pie
'''圆环图'''
# 输入标签
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","鞋子"]
# 输入各标签数据
v1=[11,12,13,10,10,10]
# 设置属性
pie=Pie("各院优秀学生人数",title_pos="center")
pie.add("",attr,v1,radius=[40,75],label_text_color=None,is_label_show=True,legend_orient="vertical",legend_pos="left")
# 生成html，打开即可
pie.render()