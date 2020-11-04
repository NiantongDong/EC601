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

if __name__ == '__main__':
    unittest.main()