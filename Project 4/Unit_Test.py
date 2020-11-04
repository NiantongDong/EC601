import unittest
import TweetAPI as TA
import Keys
import json

api = TA.Authorization_Setup()
class TestSum(unittest.TestCase):
    def test_homeline(self):
        with open('tweets.json','r') as f:
            data = json.load(f)
        self.assertEqual(TA.GET_My_Home_tweets(api),data,"Error")
    def test_user_time_line(self):
        with open('user_tweets.json','r') as f:
            data = json.load(f)
        with open('hometimeline.json','r') as f:
            data2 = json.load(f)
        #Correct user ID
        self.assertEqual(TA.Get_User_Timeline(api,'BU_ece',10),data,"Error")
        #Incorrect user ID -> Shold throw exception -> return False
        self.assertEqual(TA.Get_User_Timeline(api,'BU_ece_',10),False,"Error")
        #Pass in username instead of ID -> return home time line
        self.assertEqual(TA.Get_User_Timeline(api,'BostonUniversity ECE',10),data2,"Error")
        #Count more than user's tweets -> My account only have 2 tweets -> return only 2 text
        self.assertEqual(TA.Get_User_Timeline(api,'NiantongD',1000),data2,"Error")
    
    # def test_Search_Tweets(self):
    #     return True

if __name__ == '__main__':
    print("Start testing")
    unittest.main()