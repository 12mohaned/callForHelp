from django.shortcuts import render
import praw
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, PunktSentenceTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer

stop_words = set(stopwords.words("english"))
punctuations=["?",":","!",".",",",";","--","-","’",";","[","]","”", "“","..","(",")"]
word_lemmatizer = WordNetLemmatizer()

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
    if(word_type == 'VBP'):
        pos = 'v'
    else:
        if (word_type == 'NN'):
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
    return output
