sentiment_dictionary = {}
for line in open(r'D:\聊天机器人课程\课件+资料\AFINN\AFINN-111.txt'):
    word, score = line.split('\t')
    sentiment_dictionary[word] =int(score)
#把这个打分表记录在⼀个Dict上以后
#跑⼀遍整个句⼦，把对应的值相加
words = {'abduction'}
total_score = sum(sentiment_dictionary.get(word,0) for word in words)
#有值就是Dict中的值，没有就是0
print(total_score)
#于是你就得到了⼀个sentiment score