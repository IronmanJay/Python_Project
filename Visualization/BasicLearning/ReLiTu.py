import random
from pyecharts import HeatMap
'''热力图'''
# 准备x轴数据
x_axis=[
    "12a","1a","2a","3a","4a","5a","6a","7a","8a","9a","10a","11a",
    "12p","1p","2p","3p","4p","5p","6p","7p","8p","9p","10p","11p",]
# 准备y轴数据
y_axis=[
    "Saturday","Friday","Thursday","Wednesday","Tuesday","Monday","Sunday"]
data=[[i,j,random.randint(0,50)] for i in range(24) for j in range(7)]
heatmap=HeatMap()
# 设置属性
heatmap.add("热力图直角坐标系",x_axis,y_axis,data,is_visualmap=True,
           visual_text_color="#000",visual_orient="horizontal")
# 生成html，打开即可
heatmap.render()