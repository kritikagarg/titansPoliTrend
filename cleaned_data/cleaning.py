import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import sys

nltk.download('stopwords')

# Load your dataset
#df = pd.read_csv('/Users/kritikagarg/Downloads/merged_donald.tsv',  sep='\t',header=None)
df = pd.read_csv(sys.argv[1],  sep='\t',header=None)


def clean_tweet(tweet):
    # Remove URLs
    tweet = re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
    
    # Replace hashtags with formatted text
    tweet = re.sub(r'#(\w+)', lambda match: ' '.join(re.findall(r'[A-Z][a-z]*|[a-z]+', match.group(1))).lower(), tweet)

    # Remove special characters except spaces
    tweet = re.sub(r'[^a-zA-Z\s]', '', tweet)  
   
    # Convert to lowercase
    tweet = tweet.lower()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tweet = ' '.join(word for word in tweet.split() if word not in stop_words)

    # Remove duplicate words
    tweet = ' '.join(sorted(set(tweet.split()), key=tweet.split().index))
    
    return tweet


#extract hashtags
def extract_hashtags(tweet):
    hashtags = re.findall(r'#\w+', tweet)
    return ' '.join(hashtags)

df['clean_tweets'] = df[2].apply(clean_tweet)

# Create a new column for hashtags extracted from the original tweets
df['hashtags'] = df[2].apply(extract_hashtags)


#df.to_csv('donald_cleaned_tweets.tsv', sep='\t', index=False, header=False)
df.to_csv(sys.argv[2], sep='\t', index=False, header=False)

#remove duplicate tweet entry
# cat donald_cleaned_tweets.tsv | cut  -f4,5,6| awk -F'\t' '!seen[$2]++ { print}' > donald_cleaned_tweets_1a.tsv