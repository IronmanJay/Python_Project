from nltk.text import TextCollection
# ⾸先,把所有的⽂档放到TextCollection类中。
# 这个类会⾃动帮你断句,做统计,做计算
corpus =TextCollection(['this is sentence one','this is sentence two','this is sentence three'])
# 直接就能算出tfidf
# (term:⼀句话中的某个term, text:这句话)
print(corpus.tf_idf('this','this is sentence four'))
# 0.444342
# 同理,怎么得到⼀个标准⼤⼩的vector来表示所有的句⼦?
# 对于每个新句⼦
new_sentence ='this is sentence five'
# 遍历⼀遍所有的vocabulary中的词:
for word in standard_vocab:
    print(corpus.tf_idf(word, new_sentence))
# 我们会得到⼀个巨⻓(=所有vocab⻓度)的向量