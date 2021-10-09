import nltk
from nltk import word_tokenize
import string
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

def clean(text):
    text = text.lower()
    printable = set(string.printable)
    text = filter(lambda x: x in printable, text) #filter funny characters, if any.
    return text

def generateVocabulary(Text):
    text = word_tokenize(Text)
    POS_tag = nltk.pos_tag(text)

    adjective_tags = ['JJ','JJR','JJS']
    lemmatized_text = []

    for word in POS_tag:
      if word[1] in adjective_tags:
          lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0],pos="a")))
      else:
          lemmatized_text.append(str(wordnet_lemmatizer.lemmatize(word[0])))

    POS_tag = nltk.pos_tag(lemmatized_text)
    stopwords = []

    wanted_POS = ['NN','NNS','NNP','NNPS','JJ','JJR','JJS','VBG','FW'] 

    for word in POS_tag:
      if word[1] not in wanted_POS:
        stopwords.append(word[0])

    punctuations = list(str(string.punctuation))
    stopwords = stopwords + punctuations

    stopword_file = open("training_data/long_stopwords.txt", "r")
    lots_of_stopwords = []

    for line in stopword_file.readlines():
       lots_of_stopwords.append(str(line.strip()))

    stopwords_plus = []
    stopwords_plus = stopwords + lots_of_stopwords
    stopwords_plus = set(stopwords_plus)

    processed_text = []
    for word in lemmatized_text:
      if word not in stopwords_plus:
         processed_text.append(word)
    vocabulary = list(set(processed_text))
    return vocabulary