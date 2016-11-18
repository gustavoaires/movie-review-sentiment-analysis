import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))

with open('/home/gustavo/git/sentiment_analysis/review_polarity/txt_sentoken/neg/cv000_29416.txt', 'r') as text_file:
    text = text_file.read()
    tokens = word_tokenize(str(text))
    tokens = [w for w in tokens if w not in stopset]
    print tokens
