import pandas as pd
from textblob import TextBlob

df = pd.read_csv('tweets_OnePiece.csv')


def subjektivitas(tr_text):
  return TextBlob(tr_text).sentiment.subjectivity

def polaritas(tr_text):
  return TextBlob(tr_text).sentiment.polarity

def hasilSentimen(nilai):
  if nilai < 0:
    return 'negatif'
  elif nilai == 0:
    return 'netral'
  else:
    return 'positif'

df['subjektivitas'] = df['translated_text'].apply(subjektivitas)
df['polaritas'] = df['translated_text'].apply(polaritas)
df['sentimen'] = df['polaritas'].apply(hasilSentimen)


print(df)


df.to_csv('tweets_OnePiece.csv', index=False)


# Calculate the percentage of positive and negative sentiments
total_tweets = len(df)
positive_tweets = len(df[df['sentimen'] == 'positif'])
negative_tweets = len(df[df['sentimen'] == 'negatif'])

percentage_positive = (positive_tweets / total_tweets) * 100
percentage_negative = (negative_tweets / total_tweets) * 100

# Print or use the percentages as needed
print(f"Percentage of Positive Sentiments: {percentage_positive:.2f}%")
print(f"Percentage of Negative Sentiments: {percentage_negative:.2f}%")
