import ast
import string
import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.stem import PorterStemmer 


# Download the 'punkt' resource
nltk.download('punkt')


df = pd.read_csv('tweets_OnePiece.csv')


def stemming_nltk(tweet):
    print(tweet)
    ps = PorterStemmer()

    do=[]

    for w in ast.literal_eval(tweet):
        dt = ps.stem(w)
        do.append(dt)

    # d_clean=[]
    d_clean=" ".join(do)
    return d_clean


df['stemming_nltk'] = df['stopwords_nltk'].apply(lambda x: stemming_nltk(x))


def stemming_sastrawi(tweet):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    # do=[]

    dt = stemmer.stem(tweet)
    # do.append(dt)

    # d_clean=[]
    # d_clean=" ".join(do)
    return dt


df['stemming_sastrawi'] = df['stopwords_sastrawi'].apply(lambda x: stemming_sastrawi(x))


print(df)


df.to_csv('tweets_OnePiece.csv', index=False)
