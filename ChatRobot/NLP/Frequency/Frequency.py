import nltk
from nltk import FreqDist
#做个词库先
corpus ='this is my sentence this is my life this is the day'

#随便tokenize⼀下
#显然,正如上⽂提到,
#这⾥可以根据需要做任何的preprocessing:
# stopwords, lemma, stemming, etc.
tokens = nltk.word_tokenize(corpus)
print(tokens)
#得到token好的word list
# ['this', 'is', 'my', 'sentence',
# 'this', 'is', 'my', 'life', 'this',# 'is', 'the', 'day']

#借⽤NLTK的FreqDist统计⼀下⽂字出现的频率
fdist = FreqDist(tokens)
#它就类似于⼀个Dict
#带上某个单词,可以看到它在整个⽂章中出现的次数
print(fdist['is'])

#好,此刻,我们可以把最常⽤的50个单词拿出来
standard_freq_vector = fdist.most_common(50)
size =len(standard_freq_vector)
print(size)
print(standard_freq_vector)
# [('is', 3), ('this', 3), ('my', 2),
# ('the', 1), ('day', 1), ('sentence', 1),
# ('life', 1)

# Func:按照出现频率⼤⼩,记录下每⼀个单词的位置
def position_lookup(v):
    res = {}
    counter =0
    for word in v:
        res[word[0]] = counter
        counter +=1
    return res
#把标准的单词位置记录下来
standard_position_dict = position_lookup(standard_freq_vector)
print(standard_position_dict)

#这时,如果我们有个新句⼦:
sentence ='this is cool'
#先新建⼀个跟我们的标准vector同样⼤⼩的向量
freq_vector = [0] * size
#简单的Preprocessing
tokens = nltk.word_tokenize(sentence)
#对于这个新句⼦⾥的每⼀个单词
for word in tokens:
    try:
        #如果在我们的词库⾥出现过
        #那么就在"标准位置"上+1
        freq_vector[standard_position_dict[word]] += 1
    except KeyError:
        #如果是个新词
        #就pass掉
        continue
print(freq_vector)
# [1, 1, 0, 0, 0, 0, 0]
#第⼀个位置代表is,出现了⼀次
#第⼆个位置代表this,出现了⼀次
