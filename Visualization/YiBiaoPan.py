from pyecharts import Gauge
'''仪表盘'''
# 设置标题
gauge=Gauge("就业率")
# 设置标签和数据
gauge.add("就业指标","完成率",66.66)
# 生成html，打开即可
gauge.render()