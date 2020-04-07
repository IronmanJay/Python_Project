
with open(r'D:\聊天机器人课程\课件+资料\alice.txt') as fo:
	txt_raw = fo.read()
		
from bs4 import BeautifulSoup
txt_bs = BeautifulSoup(txt_raw, 'lxml').get_text()


import nltk
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences_raw = tokenizer.tokenize(txt_bs)

sntncs = []
stops = set(nltk.corpus.stopwords.words('english'))
import re
for sntnc in sentences_raw:
    lttr_only = re.sub('[^a-zA-z]', " ", sntnc)
    wrds = lttr_only.lower().split()
    wrds_mnng = [w for w in wrds if not w in stops]
    sntncs += [wrds_mnng]
    
from gensim.models import word2vec
num_features = 1000
min_word_count = 10
num_workers = 4
size = 256
window = 5

model = word2vec.Word2Vec(sntncs, workers=num_workers, \
        size=num_features, min_count=min_word_count, \
        window=window)
model.save('lol.save')        
        
        