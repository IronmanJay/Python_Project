from nltk.stem.porter import PorterStemmer

porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('maximum'))
print(porter_stemmer.stem('presumably'))
print(porter_stemmer.stem('provision'))

p = PorterStemmer()
print(p.stem('went'))
print(p.stem('wenting'))