from nltk.corpus import stopwords
# 先token⼀把，得到⼀个word_list
# ...
# 然后filter⼀把
word_list = {'a','b','c'}
filtered_words = [word for word in word_list if word not in stopwords.words('english')]