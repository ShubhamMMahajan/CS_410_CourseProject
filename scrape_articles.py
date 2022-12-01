import os
from collections import defaultdict
import re
import math

data_folder = "data"
data_files = os.listdir(os.path.join(os.getcwd(),data_folder))
#print(data_files)

tf = defaultdict(int)
df = defaultdict(int)
doc_count = 0
def calculate_tf(article_text):
	tokens = re.split(r'[\W_]+', article_text.lower().encode('ascii',errors='ignore').decode(errors='ignore'))
	for token in tokens:
		tf[token] += 1

def calculate_df(article_text):
	tokens = re.split(r'[\W_]+', article_text.lower().encode('ascii',errors='ignore').decode(errors='ignore'))
	tokens = list(set(tokens))
	for token in tokens:
		df[token] += 1

def write_tf_file():
	tf_file = open("tf.txt", 'w')
	for word, count in sorted(tf.items(),key=lambda x: x[1],reverse=True):
		tf_file.write(word + "\t" + str(count) + "\n")
	tf_file.close()

def write_idf_file():
	idf_file = open("idf.txt", 'w')
	for word, doc_freq in sorted(df.items(),key=lambda x: x[1],reverse=True):
		idf = math.log(doc_count / doc_freq, 2)
		idf_file.write(word + "\t" + str(idf) + "\n")

for file in data_files:
	article_file = open(os.path.join(os.getcwd(),data_folder,file), 'r')
	articles = article_file.readlines()
	article_text_total = "";
	for i in range(1, len(articles)): # ignore header
		article_text = " ".join(articles[i].split(",")[2:]) 
		article_text_total += article_text
		doc_count += 1
		calculate_df(article_text)
		if i % 10000 == 0:
			print("i =", i)
	calculate_tf(article_text_total)
	article_file.close()
	print("finished parsing", file)


write_tf_file()
write_idf_file()
