from nltk.classify import NaiveBayesClassifier
#随⼿造点训练集
s1 ='this is a good book'
s2 ='this is a awesome book'
s3 ='this is a bad book'
s4 ='this is a terrible book'
def preprocess(s):
    # Func:句⼦处理
    #这⾥简单的⽤了split(),把句⼦中每个单词分开
    #显然还有更多的processing method可以⽤
    return {word: True for word in s.lower().split()}
    # return⻓这样:
    # {'this': True, 'is':True, 'a':True, 'good':True, 'book':True}
    #其中,前⼀个叫fname,对应每个出现的⽂本单词;
    #后⼀个叫fval,指的是每个⽂本单词对应的值。
    #这⾥我们⽤最简单的True,来表示,这个词『出现在当前的句⼦中』的意义。
    #当然啦,我们以后可以升级这个⽅程,让它带有更加⽜逼的fval,⽐如word2vec
# #把训练集给做成标准形式
training_data = [[preprocess(s1),'pos'],
                 [preprocess(s2),'pos'],
                 [preprocess(s3),'neg'],
                 [preprocess(s4),'neg']]
#喂给model吃
model = NaiveBayesClassifier.train(training_data)
#打出结果
print(model.classify(preprocess('this is a good book')))