import tweepy
import Keys #All my keys in local file
import sys
import json #To write file as json format

def Authorization_Setup():
    auth = tweepy.OAuthHandler(Keys.consumer_key, Keys.consumer_secret)
    auth.set_access_token(Keys.access_token, Keys.access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api

#Print out tweets' text
def Display_tweets(Input_list):
    tweet_text_list = []
    for status in Input_list:
        tweet_text_list.append(status.text)
        # print(status.text,end ="\n\n")
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
def GET_Search_Tweets(Local_API,Target_content,search_type,Count_Number,Time):
    Result_Tweets = Local_API.search(q=Target_content,result_type = search_type,count = Count_Number,until = Time)
    Display_tweets(Result_Tweets)
    Write_tweets_to_File(Result_Tweets,'Search_tweets')
    return Result_Tweets

#Search tweets based on Hashtag and time.
def GET_Hashtag_Search_Tweets(Local_API,Hashtag,Count_Number,Time_before):
    Hashtag_Tweets = tweepy.Cursor(Local_API.search,q=Hashtag,count=Count_Number,since=Time_before)
    Write_tweets_to_File(Hashtag_Tweets.items(),'Hashtag_Tweets')
    for status in Hashtag_Tweets.items():
        print(status.text)
    return Hashtag_Tweets

if __name__ == "__main__":
    API = Authorization_Setup()
    Home_Tweets = GET_My_Home_tweets(API)
    User_Tweets = Get_User_Timeline(API,"NiantongD",1000) #Use Boston University ECE department twitter as example.
    # Result_Tweets = GET_Search_Tweets(API,"Boston University","recent",10,"2020-09-26")
    # GET_Hashtag_Search_Tweets(API,"#Trump",5,"2020-09-30")
