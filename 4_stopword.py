import string
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import nltk


# Download the 'punkt' resource
nltk.download('punkt')


df = pd.read_csv('tweets_OnePiece.csv')


def stopword_nltk(tweets):
    listStopword =  set(stopwords.words('indonesian'))

    tweets = tweets.translate(str.maketrans('','',string.punctuation)).lower()
 
    tweets = nltk.tokenize.word_tokenize(tweets)
 
    removed = []
    for t in tweets:
        if t not in listStopword:
            removed.append(t)
    return removed


df['stopwords_nltk'] = df['tokenize'].apply(stopword_nltk)


def stopword_sastrawi(tweets):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
 
    tweets = tweets.translate(str.maketrans('','',string.punctuation)).lower()
    stop = stopword.remove(tweets)
    tokens = nltk.tokenize.word_tokenize(stop)
    return tokens


df['stopwords_sastrawi'] = df['clean'].apply(stopword_nltk)


print(df)


df.to_csv('tweets_OnePiece.csv', index=False)
