import tweepy
# import Keys #All my keys in local file
import sys
import json #To write file as json format
import os

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
def Authorization_Setup():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
    except Exception:
        sys.exit("Reach limit, cannot connect to API")

#Print out tweets' text
def Display_tweets(Input_list):
    tweet_text_list = []
    for status in Input_list:
        tweet_text_list.append(status.text)
        print(status.text,end ="\n\n")
    return tweet_text_list

#Write tweets information to file as json format.
def Write_tweets_to_File(Input_list,target_filename):
    data = []
    filename = "%s.json" % target_filename
    Tweets_text = open(filename, 'w') 
    for status in Input_list:
        # json.dump(status._json,Tweets_text,indent = 4)
        data.append(status._json)
    json.dump(Display_tweets(Input_list),Tweets_text)
    Tweets_text.close
    return Display_tweets(Input_list)


def Write_tweets_to_File_cursor(Input_list,target_filename):
    data = []
    filename = "%s.json" % target_filename
    Tweets_text = open(filename, 'w') 
    for status in Input_list:
        # json.dump(status._json,Tweets_text,indent = 4)
        data.append(status.text)
    json.dump(data,Tweets_text)
    Tweets_text.close
    return data
    
#Get all of tweets from my home page.
def GET_My_Home_tweets(Local_API):
    My_Home_tweets = Local_API.home_timeline()
    # Display_tweets(My_Home_tweets)
    Write_tweets_to_File(My_Home_tweets,'tweets')
    return Write_tweets_to_File(My_Home_tweets,'tweets')

#Get certain number of tweets from a single twitter account.
def Get_User_Timeline(Local_API,User_ID,Count_Number):
    try:
        user_tweets_list = Local_API.user_timeline(User_ID,count = Count_Number)
        # Display_tweets(user_tweets)
        result = Write_tweets_to_File(user_tweets_list,'user_tweets')
        return result
    except Exception:
        return False

#Search and return tweets based on input txt and time.
def GET_Search_Tweets(Local_API,Target_content,search_type,Count_Number,Time,filename):
    try:
        Result_Tweets = Local_API.search(q=Target_content,result_type = search_type,count = Count_Number,until = Time)
        # Display_tweets(Result_Tweets)
        result = Write_tweets_to_File(Result_Tweets,filename)
        return result
    except Exception:
        return False

#Search tweets based on Hashtag and time.
def GET_Hashtag_Search_Tweets(Local_API,Hashtag,Count_Number,Time_before,filename):
    Hashtag_Tweets = tweepy.Cursor(Local_API.search,q=Hashtag,count=Count_Number,since=Time_before)
    # Display_tweets(Hashtag_Tweets.items())
    result = Write_tweets_to_File_cursor(Hashtag_Tweets.items(),filename)
    return result

if __name__ == "__main__":
    API = Authorization_Setup()
    Home_Tweets = GET_My_Home_tweets(API)
    User_Tweets = Get_User_Timeline(API,"BU_ece",10) #Use Boston University ECE department twitter as example.
    Result_Tweets = GET_Search_Tweets(API,"Boston University","recent",10,"2020-11-1","test_Search_1")
    Result_Tweets2 = GET_Search_Tweets(API,"Boston University","recent",10,"2021-12-12","test_Search_2")
    Result_Hashtag_1 = GET_Hashtag_Search_Tweets(API,"#Boston",1,"2020-11-01","test_Hashtag_1")
    