import nltk
import os
import csv
import re
import pandas
import operator
import math
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sets import Set

stemmer = SnowballStemmer("english")
stopset = set(stopwords.words("english"))
symbols = ["\"", "\'", "!", "?", ".", "," , ";", ">", "_", "<", "-", "[",
			"]", "{", "}", "'s", "\/", "\\", "^", "~", "'", "`", "``",
			":", "(", ")", "@", "#", "$", "%", "&", "*", "=", "+"]

pos_files = []
neg_files = []

incomplete_path = "/home/gustavo/git/sentiment_analysis/review_polarity/txt_sentoken/"

#loading neg_files
file_names = os.listdir(incomplete_path + "neg")
neg_files = file_names[0:700]
neg_files_test_set = file_names[701:1000]

#loading pos_files
file_names = os.listdir(incomplete_path + "pos")
pos_files = file_names[0:700]
pos_files_test_set = file_names[701:1000]

training_set = []

#path to save training set
training_set_path = '/home/gustavo/git/sentiment_analysis/training_set.csv'

#reads the file
def read_file(path, label):
	with open(path, 'r') as text_file:
		text = text_file.read()
		tokens = str(text).split()
		valid_tokens = [w for w in tokens if (w not in stopset) and (w not in symbols) and (re.search('[a-zA-Z]', w))]
		tokens = []
		for token in valid_tokens:
			tokens.append(str(stemmer.stem(token)))
		training_set.append((tokens, label))
		
#iterate all file names to read and create tuples
def get_file_name():
	for i in range(0, 700):
		path = incomplete_path + "neg/" + neg_files[i]
		read_file(path, 'neg')
		path = incomplete_path + "pos/" + pos_files[i]
		read_file(path, 'pos')
	
#save data (tokens with labels) into file
def write_training_set():
	with open(training_set_path, 'wb') as csvfile:
		writer = csv.writer(csvfile)
		for row in training_set:
			data = []
			for w in row[0]:
				data.append(w)
			data.append(row[1])
			writer.writerow(data)

#data frame with the frequency			
df = pandas.DataFrame(columns=['neg','pos'])

def count_freq():
	words_set = Set()
	for item in training_set:
		label = item[1]
		text = item[0]
		for word in text:
			if word not in words_set:
				words_set.add(word)
				df.loc[word] = [0,0]
				df.ix[word][label] += 1
			else:
				df.ix[word][label] += 1

#path to data frame csv
data_frame_path = '/home/gustavo/git/sentiment_analysis/data_frame.csv'

#write data frame into csv file
def write_data_frame():
	df.to_csv(data_frame_path, sep='\t')
	
#read data frame from csv file	
def read_data_frame():
	df.read_csv(data_frame_path, sep='\t')
	
def main():
	#get_file_name()
	#write_training_set()
	#count_freq()
	#write_data_frame()

main()

"""	
	code to read file training_set so we can apply naive bayes
	this code should go into python file that reads the tokens (better if it is not this one)
"""
#with open(training_set_path, 'rb') as csvfile:
#	spamreader = csv.reader(csvfile)
#	for row in spamreader:
#		<training_set>.append((row[0:-1], row[-1]))
