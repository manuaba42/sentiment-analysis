import pandas as pd

# Read the CSV file into a DataFrame
csv_file_path = 'tweets_OnePiece.csv'
df = pd.read_csv(csv_file_path)

# Specify columns to delete
columns_to_delete = ['id', 'id_str', 'truncated', 'display_text_range', 'entities', 'metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'geo', 'coordinates', 'place', 'contributors', 'retweeted_status', 'is_quote_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'lang', 'possibly_sensitive', 'extended_entities', 'quoted_status_id', 'quoted_status_id_str', 'quoted_status', 'withheld_scope', 'withheld_in_countries', 'withheld_copyright', 'remove_user', 'case_folding', 'clean', 'tokenize', 'stopwords', 'stemming']

# Check if the columns exist in the DataFrame
existing_columns = set(df.columns)
columns_to_delete = [col for col in columns_to_delete if col in existing_columns]

if columns_to_delete:
    # Drop the specified columns
    df.drop(columns=columns_to_delete, inplace=True)
    
    # Save the modified DataFrame back to the CSV file
    df.to_csv(csv_file_path, index=False)
    
    print(f"Columns {', '.join(columns_to_delete)} deleted successfully.")
else:
    print("No matching columns found in the DataFrame.")
