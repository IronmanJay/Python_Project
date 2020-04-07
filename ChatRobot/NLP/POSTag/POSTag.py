import nltk

text = nltk.word_tokenize('what does the fox say')
print(text)
print(nltk.pos_tag(text))