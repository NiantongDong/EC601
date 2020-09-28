# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

# Instantiates a client
client = language.LanguageServiceClient()

#Import Tweets result file.
with open("tweets.json") as f:
    data = json.loads(f.read()) 
Sentiment_output = open("tweets_sentiment.txt","w")
#Analyze each tweet text
for tweet in data:
    text = tweet['text']
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    #Call API to analyze text.
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    #Write result to file
    Sentiment_output.write("Text:" + text +"\n")
    Sentiment_output.write("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude)+"\n")