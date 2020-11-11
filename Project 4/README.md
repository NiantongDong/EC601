# Project 4
## Twitter API
To start unit test, make sure you install the latest tweepy . Run this line to update it. 

```
pip install tweepy
```

Then, the unit test file name is "Unit_Test.py". Before you run it, please run the "TweetAPI.py" to generate correct output for the unit test

```
py TweetAPI.py
py Unit_Test.py
```

You may need keys to access twitter API. If you can't access the secret key, you can use your own keys. Make sure you create a file name "**Keys.py**" in the same directory and input your key in this format. My script should import it automatically and use it to do the authentication. Also, if the script stuck, you may need to wait for a while because it sometimes exceed the API call limit and my script will wait until it return normal again.

```python
consumer_key =''
consumer_secret = ''
access_token = ''
access_token_secret = ''
Bearer_token =''
```



## Google NLP

I only finished unit test for Twitter API because I can't use the Google NLP library due to "ImportError: No module named grpc". I try a lot of method including "pip install grpcio" but they all won't work. In that case, I may not able to run the unit test for Google NLP API.
However, Here is the idea about how to test it.
First, I will give it a single sentence with any possible sentiment on it. I try to analyze it for , like, 100, times and compare to the result. If the result is consistent, it pass the test. I assume that sentence should contains mixed positive and negtive sentitments and the overall score should be 0 if that is possbie.
Then, I may use some netural sentence from internet to analyze, for example, other's sentiment analysis content. It should returns the same result as the others'. I also need to run it for a few times to see if the result is consistent.
Finally, I want to use a huge content, for example, a short story, to test its capability. Try to reach the API limit and see how good is the performance.
I will try to set up the environment again and hopefully I can finish it without any issues