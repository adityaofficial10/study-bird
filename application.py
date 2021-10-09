import os
import sys
from flask import Flask, jsonify, make_response, redirect, request
from flask_cors import CORS
import nltk
import tika
tika.initVM()

try:    
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
except Exception as exp:
    print(f" ERROR {exp}")
    raise Exception("NLTK download failed")

basedir = os.path.abspath(os.path.dirname(__file__))

application = Flask(__name__)
CORS(application)

application.debug = True

if os.environ.get('ENV') is None:
    application.debug = True
elif os.environ.get('ENV') == 'prod':
    application.debug = False

from text_summary import SummarizerNLTK
from keyword_extractor import generateVocabulary
from resume_parser import generate

@application.route('/test')
def test():
    return "Server running!"

@application.route('/text-analyser', methods=['POST'])
def summarize():
    text = request.form['text-stream']
    summ = SummarizerNLTK().summary(text=text)
    keywords = generateVocabulary(Text=text)
    data = {
        'summary': summ,
        'keywords': keywords,
        'status': "Success"
    }
    return jsonify(data)

@application.route('/resume-parser', methods=['POST'])
def generate():
    resume = request.form['resume']
    questions = generate(resume)
    return jsonify({'questions': questions})

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000)