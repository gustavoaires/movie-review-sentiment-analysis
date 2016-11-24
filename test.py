import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))
symbols = ["\"", "\'", "!", "?", ".", "," , ";", ">", "_", "<", "-", "[", "]", "{", "}", "'s", "\/", "\\", "^", "~", "'", "`", "``", ":", "(", ")", "@", "#", "$", "%", "&"]

files_pos = []
files_neg = []

#fill files_neg
files_names = os.listdir("/home/gustavo/git/sentiment_analysis/review_polarity/txt_sentoken/neg")
files_neg = files_names[0:299]

#fill files_pos
files_names = os.listdir("/home/gustavo/git/sentiment_analysis/review_polarity/txt_sentoken/pos")
files_pos = files_names[0:299]

tokens_with_labels = []

#reads the file
def read_file(path, label):
	with open(path, 'r') as text_file:
		text = text_file.read()
		tokens = str(text).split()
		tokens = [w for w in tokens if w not in stopset]
		tokens = [w for w in tokens if w not in symbols]
		tokens_with_labels.append((tokens, label))
		
#iterate the name files to read and create tuples		
for i in range(0, 1):
	path = "/home/gustavo/git/sentiment_analysis/review_polarity/txt_sentoken/neg/" + files_neg[i]
	read_file(path, 'neg')
	path = "/home/gustavo/git/sentiment_analysis/review_polarity/txt_sentoken/pos/" + files_pos[i]
	read_file(path, 'pos')

print tokens_with_labels
