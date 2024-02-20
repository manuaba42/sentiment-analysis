import string
import pandas as pd
import numpy as np
import nltk

# Download the 'punkt' resource
nltk.download('punkt')

df = pd.read_csv('tweets_OnePiece.csv')

def token(tweets):
    tweets = nltk.tokenize.word_tokenize(tweets)

    tweets = [word.lower() for word in tweets if word.isalpha()] 
    
    return tweets
df['tokenize'] = df['clean'].apply(token)


print(df)


df.to_csv('tweets_OnePiece.csv', index=False)
