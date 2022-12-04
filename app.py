from flask import Flask,render_template,request
from nltk.corpus import wordnet
from collections import defaultdict
import re
app = Flask(__name__)

tf_file = open("tf.txt", "r")
tf_data = tf_file.readlines()
word_count = defaultdict(int)
for line in tf_data:
    word, count = line.split("\t")
    word_count[word] = int(count)

@app.route('/form', methods = ['POST', 'GET'])
def form():
    return render_template('form.html')

def process_data(form_data):
    complex_text = form_data["complexText"]
    tokens = re.split(r'[\W_]+', complex_text.lower().encode('ascii',errors='ignore').decode(errors='ignore'))
    simple_text = ""
    for token in tokens:
        easy_word = token
        easy_word_count = word_count[token]
        for synonyms in wordnet.synsets(token):
            for synonym in synonyms.lemmas():
                word = synonym.name()
                if word_count[word] > easy_word_count:
                    easy_word = word
                    easy_word_count = word_count[word]
        simple_text += easy_word + " "
    return simple_text


@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        simple_text = process_data(form_data)
        text_dict = dict()
        text_dict["complexText"] = form_data["complexText"]
        text_dict["simpleText"] = simple_text
        return render_template('data.html',form_data = text_dict)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
