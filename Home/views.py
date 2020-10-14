from django.shortcuts import render
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import NaiveBayesClassifier, classify

import pickle
stop_words = set(stopwords.words("english"))
punctuations=["?",":","!",".",",",";","--","-","’",";","[","]","”", "“","..","(",")"]
word_lemmatizer = WordNetLemmatizer()


def Home(request):
    classifier = de_serialize()
    text = Tokenize('I hurt myself today to see if i can feel i focus on the pain')
    print(classifier.classify(text))

    return render(request, template_name = 'Home.html')
#check if a word is a stop word
def is_stopword(word):
    if word in stop_words:
        return True
    return False

#check if a word is a punctuation
def is_Punk(word):
    if word in punctuations :
        return True
    return False

#returning the verb to it's origin
def lemmatizing(word, word_tag):
    if(word_tag == 'VBP'):
        pos = 'v'
    else:
        if (word_tag == 'NN'):
            pos = 'n'
        else:
            pos = 'a'
    word = word_lemmatizer.lemmatize(word, pos = pos)
    return word

#check the weight of the word wether it's important or not
def check_importance(word_type):
    if (word_type == 'PRP' or word_type == 'PRP$'
        or word_type == 'WRB' or word_type == 'EX'
        or word_type == 'CD' or word_type == 'MD'
        or word_type == 'WP'or word_type == 'POS'
        or word_type == 'CC' or word_type == 'TO'
        or word_type == 'WDT'or word_type == 'WP$'
        or word_type == 'UH' or word_type == 'FW'
        or word_type == 'IN' or word_type == 'DT'
        or word_type == 'VBP'):
        return False;
    return True

#break the sentence into words
def Tokenize(Text):
    output = []
    Tokenized_sent = nltk.pos_tag(word_tokenize(Text))
    for word, word_type in Tokenized_sent:
        if not is_stopword(word):
            if not is_Punk(word):
                if check_importance(word_type):
                    word = lemmatizing(word, word_type)
                    output.append(word)
    output = dict([token, True] for token in output)
    return output

def de_serialize():

    pickled_model = open('C://Users//mohan//callForHelp//Home//naive_bayes_model.sav', 'rb')
    naive_bayes_classifier = pickle.load(pickled_model)
    pickled_model.close()
    return naive_bayes_classifier
