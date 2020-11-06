import unittest
import TweetAPI as TA
# import Keys
import json
import sys

api = TA.Authorization_Setup()
class TestSum(unittest.TestCase):
    def test_homeline(self):
        with open('tweets.json','r') as f:
            data_home = json.load(f)
        self.assertEqual(TA.GET_My_Home_tweets(api),data_home,"Error")
    def test_user_time_line(self):
        with open('user_tweets.json','r') as f:
            data_user = json.load(f)
        with open('hometimeline.json','r') as f:
            data_user2 = json.load(f)
        #Correct user ID
        self.assertEqual(TA.Get_User_Timeline(api,'BU_ece',10),data_user,"Error")
        #Incorrect user ID -> Shold throw exception -> return False
        self.assertEqual(TA.Get_User_Timeline(api,'BU_ece_',10),False,"Error")
        #Pass in username instead of ID -> return home time line
        self.assertEqual(TA.Get_User_Timeline(api,'BostonUniversity ECE',10),data_user2,"Error")
        #Count more than user's tweets -> My account only have 2 tweets -> return only 2 text
        self.assertEqual(TA.Get_User_Timeline(api,'NiantongD',1000),data_user2,"Error")
    
    def test_Search_Tweets(self):
        with open('test_Search_1.json','r') as f:
            data_search_1 = json.load(f)
        with open('test_Search_2.json','r') as f2:
            data_search_2 = json.load(f2)
        #Expected behaviour -> Right argument -> return text
        self.assertEqual(TA.GET_Search_Tweets(api,"Boston University","recent",10,"2020-11-1","test_Search_result_1"),data_search_1,"Error")
        #Wrong date -> The argument indicate "until" date ->The API return the tweets before that date 
        self.assertEqual(TA.GET_Search_Tweets(api,"Boston University","recent",10,"2021-12-12","test_Search_result_2"),data_search_2,"Error")
        #Content not found -> always found something.

    def test_Hashtag_Search(self):
        with open('test_Hashtag_1.json','r') as f:
            data_Hashtag_1 = json.load(f)
        #Expected behaviour -> right argument
        #change to 1 to aviod exceeding search limit.
        self.assertEqual(TA.GET_Hashtag_Search_Tweets(api,"#Boston",1,"2020-11-01","result_Hashtag_1"),data_Hashtag_1,"Error")
        #Hashtag search always return something, I am not sure what I to test.

    #Google API test


if __name__ == '__main__':
    print("Start testing")
    print('TweetAPI testing')
    unittest.main()