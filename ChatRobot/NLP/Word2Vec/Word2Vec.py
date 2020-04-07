'''
#简单的⽂字预处理：

# 1.去除HTML
#这⾥⽤到BeautifulSoup这个库，
#当然，这种简单的事情，也可以⾃⼰做个字符串运算解决
from bs4 import BeautifulSoup
beautiful_text =BeautifulSoup(raw_text).get_text()
#

# 2.把⾮字⺟的去除掉
#这⾥可以⽤正则表达式解决
import re
letters_only = re.sub("[^a-zA-Z]"," ", beautiful_text)
#

# 3.全部⼩写化
words = letters_only.lower().split()
#

# 4.去除stopwords
#这⾥⽤到NLTK
from nltk.corpus import stopwords
stops =set(stopwords.words("english"))
meaningful_words = [w for w in words if not w in stops]

#⾼阶⽂字处理：
# 5. Lemmatization
#
#这个⽐较复杂，下次NLTK的时候讲

# 6.搞回成⼀⻓串string
return(" ".join( meaningful_words ))

# tokenizor:把原来的string训练集，变成list of lists：
#简单点的话，可以⽤这个：
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
print (sentences)
'''

#现在进⼊正题，w2v。
#我们⽤Gensim这个库来做，很⽅便。
from gensim.models import word2vec
#先设⼀下param
num_features =1000#最多多少个不同的features
min_word_count =10#⼀个word，最少出现多少次才被计⼊
num_workers =4#多少thread⼀起跑（快⼀点⼉）
size =256# vec的size
window =5#前后观察多⻓的“语境”

#跑起来
model = word2vec.Word2Vec(sentences,'''size=size''', workers=num_workers, size=num_features, min_count = min_word_count, window = window)
#你可以save下来
model.save('LOL.save')
#⽇后再load回来
model = word2vec.Word2Vec.load('LOL.save')

#当然你们也许会看到⾕歌也提供了⾃⼰的News包：
#要load其他语⾔train出来的⽂件（⽐如C)的Bin或者text⽂件
#那就这样：
model = Word2Vec.load_word2vec_format('google_news.txt', binary=False)# C text format
model = Word2Vec.load_word2vec_format('google_news.bin', binary=True)# C binary format
#⼏个常⽤的⽤法：
# woman + king - man = queen
model.most_similar(positive=['woman','king'], negative=['man'])
[('queen',0.50882536), ...]
#求两个词的senmatics相似度
model.similarity('woman','man')
0.73723527
#就更dict⼀样使⽤你train好的model
model['computer']
array([-0.00449447, -0.00310097,0.02421786, ...], dtype=float32)
#现在你可以把这个model包装起来。把你所有的sentences token过⼀遍
def w2vmodel(sentences):
    ...
    return vec

# 这个时候你会发现，我们的vec是针对每个word的。⽽我们的训练集是sen和label互相对应的，
# ⼯业上，到了这⼀步，有三种解决⽅案：
# 1.平均化⼀个句⼦⾥所有词的vec。
# sen_vec = [vec, vec, vec, ...] / n
# 2.排成⼀个⼤matrix (M * N)，等着CNN来搞
# [ vec | vec | vec | vec | ... ]
# 3.⽤Doc2Vec。这是基于句⼦的vec，跟word2vec差不多思路，⽤起来也差不多。
# 只对⻓篇⼤⽂章效果好。对头条新闻，twitter这种的东⻄，就不⾏了。每个“篇”的句⼦太少。
# 具体可以看gensim。
# Anyway,这⼀步完成后，你会对于每个训练集的X，得到⼀个固定⻓度的vec或者matrix
# 接下来的事情，⼤家就可以融会贯通了。
# ⽐如，可以⽤前⾯冯⽼师讲的RF跑⼀遍做classification。
