import re
import string
import pandas as pd
import numpy as np

df = pd.read_csv('tweets_OnePiece.csv')

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for I in r:
        input_txt = re.sub(I, '', input_txt)
    return input_txt
df['remove_user'] = np.vectorize(remove_pattern)(df['full_text'], '@[\w]*')
# fungsinya untuk menghilangkan @ @ user pada twit hasil yg diambil sebelumnya


def casefolding(tweet):
    # Convert to lowercase
    tweet = tweet.lower()
    
    # Remove leading and trailing whitespaces
    tweet = tweet.strip()
    
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Remove user mentions (assuming 'remove_user' does this)
    tweet = re.sub(r'@[A-Za-z0-9]+', '', tweet)
    
    # Remove punctuation (including more comprehensive list)
    tweet = re.sub(r'[^\w\s]', '', tweet)
    
    return tweet


df['case_folding'] = df['remove_user'].astype(str).apply(casefolding)
# case flding gunanya untuk membuat semua jadi lowercase dan beberapa simbol" aneh


def remove_emojis(text):
    """
    Remove emojis from the given text.
    """
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)


def cleansing (tweet):

    tweet = re.sub('rt ', '', (tweet))

    # Remove URLs
    tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' URL ', tweet)

    # Replace numbers with 'NUM'
    tweet = re.sub(r'\d+', '', tweet)

    # Remove unnecessary single characters
    tweet = re.sub(r'\b\w\b', ' ', tweet)

    # Remove non-alphanumeric characters
    tweet = re.sub(r'\b[^0-9A-Za-z \t]\b', ' ', tweet)

    # Remove multiple whitespaces
    tweet = re.sub(r'\s+', ' ', tweet)

    # Emoji removal (assuming emoji_pattern is defined)
    tweet = remove_emojis(tweet)

    tweet = tweet.translate(str.maketrans("","",string.punctuation))

    # Strip leading and trailing whitespaces
    tweet = tweet.strip()
    return tweet


df['clean'] = df['case_folding'].apply(lambda x: cleansing(x))
# cleansing remove symbol gk penting dan icon tidak penting


df.drop_duplicates(subset="clean", keep=False, inplace= True)
# untuk ngilangin twit duplikat


print(df)


df.to_csv('tweets_OnePiece.csv', index=False)
