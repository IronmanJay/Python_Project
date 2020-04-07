from pyecharts import Funnel
'''漏斗图'''
# 输入标签
attr=["机械","曙光","人艺","冶金","管理","外语"]
# 输入标签对应的数据
value=[140,120,100,80,60,40,20]
# 设置标题
funnel=Funnel("各院优秀学生人数")
# 设置属性
funnel.add("人数",attr,value,is_label_show=True,label_pos="inside",label_text_color="#fff")
# 生成html，打开即可
funnel.render()