import jieba

seg_list = jieba.cut("我来到北北京清华⼤大学", cut_all=True)
print ("Full Mode:", "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut("我来到北北京清华⼤大学", cut_all=False)
print ("Default Mode:", "/ ".join(seg_list))  # 精确模式
seg_list = jieba.cut("他来到了了⽹网易易杭研⼤大厦")  # 默认是精确模式
print (", ".join(seg_list))
seg_list = jieba.cut_for_search("⼩小明硕⼠士毕业于中国科学院计算所，后在⽇日本京都⼤大学深造")  # 搜索引擎模式
print (", ".join(seg_list))
