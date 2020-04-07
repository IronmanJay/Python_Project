from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('dogs'))
print(wordnet_lemmatizer.lemmatize('churches'))
print(wordnet_lemmatizer.lemmatize('aardwolves'))
print(wordnet_lemmatizer.lemmatize('abaci'))
print(wordnet_lemmatizer.lemmatize('hardrook'))

# 没有POS Tag，默认是NN名词
print(wordnet_lemmatizer.lemmatize('are'))
print(wordnet_lemmatizer.lemmatize('is'))

# 加上POS Tag
print(wordnet_lemmatizer.lemmatize('is',pos='v'))
print(wordnet_lemmatizer.lemmatize('are',pos='v'))