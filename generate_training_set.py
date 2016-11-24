import nltk
import os
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))
symbols = ["\"", "\'", "!", "?", ".", "," , ";", ">", "_", "<", "-", "[",
			"]", "{", "}", "'s", "\/", "\\", "^", "~", "'", "`", "``",
			":", "(", ")", "@", "#", "$", "%", "&", "*", "=", "+"]

files_pos = []
files_neg = []

incomplete_path = "/home/gustavo/git/sentiment_analysis/review_polarity/txt_sentoken/"

#fill files_neg
files_names = os.listdir(incomplete_path + "/neg")
files_neg = files_names[0:700]

#fill files_pos
files_names = os.listdir(incomplete_path + "/pos")
files_pos = files_names[0:700]

tokens_with_labels = []

#reads the file
def read_file(path, label):
	with open(path, 'r') as text_file:
		text = text_file.read()
		tokens = str(text).split()
		tokens = [w for w in tokens if w not in stopset]
		tokens = [w for w in tokens if w not in symbols]
		tokens_with_labels.append((tokens, label))
		
#iterate all file names to read and create tuples
for i in range(0, 700):
	path = incomplete_path + "neg/" + files_neg[i]
	read_file(path, 'neg')
	path = incomplete_path + "pos/" + files_pos[i]
	read_file(path, 'pos')
	
#save data (tokens with labels) into file
with open('/home/gustavo/git/sentiment_analysis/tokens_labels.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	for row in tokens_with_labels:
		data = []
		for w in row[0]:
			data.append(w)
		data.append(row[1])
		writer.writerow(data)
print tokens_with_labels

"""	
	code to read file
	this code should go into python file that reads the tokens (better if is not this one)
"""
#with open('/home/gustavo/git/sentiment_analysis/tokens_labels.csv', 'rb') as csvfile:
#	spamreader = csv.reader(csvfile)
#	for row in spamreader:
#		<storage-tokens-matriz>.append((row[0:-1], row[-1]))
