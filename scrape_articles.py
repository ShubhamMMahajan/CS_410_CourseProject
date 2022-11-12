import os
from collections import defaultdict
import re

data_folder = "\data"
data_files = os.listdir(os.getcwd() + data_folder)
#print(data_files)

tf = defaultdict(int)

def calculate_tf(article_text):
	tokens = re.split(r'[\W_]+', article_text.lower().encode('ascii',errors='ignore').decode())
	for token in tokens:
		tf[token] += 1

def write_tf_file():
	tf_file = open("tf.txt", 'w')
	for word, count in sorted(tf.items(),key=lambda x: x[1],reverse=True):
		tf_file.write(word + "\t" + str(count) + "\n")
	tf_file.close()

for file in data_files:
	article_file = open(os.getcwd() + data_folder + "/" + file, 'r')
	articles = article_file.readlines()
	article_text = "";
	for i in range(1, len(articles)): # ignore header
		article_text += " ".join(articles[i].split(",")[2:])
		if i % 10000 == 0:
			print("i =", i)
	calculate_tf(article_text)
	article_file.close()
	print("finished parsing", file)


write_tf_file()
