# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json


def Analyze(text_list):
    # Instantiates a client
    client = language.LanguageServiceClient()
    Result = []
    #Import Tweets result file.
    # with open(Json_file) as f:
    #     data = json.loads(f.read()) 
    Sentiment_output = open("Interface_tweets_sentiment.txt","w")
    #Analyze each tweet text
    for tweet in text_list:
        # text = tweet['text']
        document = types.Document(
            content=tweet,
            type=enums.Document.Type.PLAIN_TEXT)
        #Call API to analyze text.
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        #Write result to file
        Sentiment_output.write("Text:" + tweet +"\n")
        Sentiment_output.write("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude)+"\n")
        #Return result
        Result.append("Text:" + tweet)
        Result.append("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

    return Result


