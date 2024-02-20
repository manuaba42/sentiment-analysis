import pandas as pd
from textblob import TextBlob
import googletrans
from googletrans import Translator

df = pd.read_csv('tweets_OnePiece.csv')

translator = Translator()

# Translate function
def translate(text):
    try:
        translation = translator.translate(text, dest='en').text
        translation = translation.replace('([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ')
        translation = translation.lower()
        print(translation)
        return translation
    except Exception as e:
        print(f"Error translating text: {e}")
        return text

# Apply translation to the 'text' column
df['translated_text'] = df['stemming_sastrawi'].apply(translate)


df.to_csv('tweets_OnePiece.csv', index=False)


# # Preprocess the translated text column
# df['translated_text'] = df['translated_text'].str.replace('([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ')
# df['translated_text'] = df['translated_text'].str.lower()

# Save the DataFrame to a new CSV file with translated text
# df.to_csv('translated_tweets_OnePiece.csv', index=False)
