from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))

with open('sentiment_test.txt', 'r') as text_file:
    text = text_file.read()
    tokens=word_tokenize(str(text))
    tokens = [w for w in tokens if not w in stopset]
    print tokens
