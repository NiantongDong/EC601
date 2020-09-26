import tweepy
import Keys #All my keys in local file
import sys
# from searchtweets import ResultStream, gen_rule_payload, load_credentials
# import yaml
# from searchtweets import collect_results
# print("Hello world!")

def Authorization_Setup():
    auth = tweepy.OAuthHandler(Keys.consumer_key, Keys.consumer_secret)
    auth.set_access_token(Keys.access_token, Keys.access_token_secret)
    api = tweepy.API(auth)
    return api

#Print out tweets' text
def Display_tweets(Input_list):
    for tweet in Input_list:
        print(tweet.text,end ="\n\n")

# def Write_tweets_to_File():
#     Tweets_text = open('tweet.json', 'w') 

#Get all of tweets from my home page.
def GET_My_Home_tweets(Local_API):
    My_Home_tweets = Local_API.home_timeline()
    Display_tweets(My_Home_tweets)
    return My_Home_tweets

# def Get_User_Timeline(Local_API):

if __name__ == "__main__":
    API = Authorization_Setup()
    Home_Tweets = GET_My_Home_tweets(API)

# Certain_tweets = api.user_timeline(User_ID,count=c)