# Project 2
Reference :
For TweetAPI.py, Most of codes are modified based on the offical tweepy tutorial.
For GoogleNLP.py, Modified from offical Google NLP tutorial.
PySimpleGUI, https://github.com/PySimpleGUI/PySimpleGUI

## Phase 1
TweetAPI:
Before run this python file, make sure you have the latest version of python. Also, you need to have Twitter develop account and relavent key to access twitter API.
I store my key locally and load it when I run this program. If you want to use your own key, please name your file "Keys.py" and use the following format.
```python
consumer_key ='Your API key/consumer key'
consumer_secret = 'Your secret API key/ consumer key'
access_token = 'Your access token'
access_token_secret = 'Your secret access token'
Bearer_token ='Your bearer token'
```

This program has imeplemented retrieving my home page tweets, retrieving speific user tweets,retrieving tweets which contain certain content, and retrieving tweets based on hashtag.

The result is stored as json format and will be used for google NLP sentiment analysis.

To run this program, use terminal to run this line
```cmd
py TweetAPI.py
```

GoogleNLP:
To set up Google NLP environment, follow the offical setup instruction.
You also need to download your key to local and set the environment varible to is.
Use the following line to do so.
If you use cmd
```
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```
Or, if you use powershell
```
$env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

Without this step , you may not able to call the API to analyze.

In my code, I only analyze the tweets from my home page. You can change it to other json file if you want.

To run this program, use terminal to run this line
```cmd
py GoogleNLP.py
```

This program will automatically output a text file which contains the result, the sentiment score and sentiment magnitude.




## Phase 2
To set up environment, you need to run this line to install GUI.
```
pip install pysimplegui
```

Then, you can search specific user timeline and choose how many tweets you want to retrieve. If the user id is not found, it will return your own timeline instead. So make sure you input the right user id.

The MVP for my program is to retrieve user tweets and analyze the sentiment. The user stories can be someone who want to know a person's recent attitude in twitter. For example, I want to know how Donald J. Trump doing recently. I can type in the user id 'realDonaldTrump' and I want to know the recent 5 tweets,or any number you want. Then, it will pop up window to show his tweets or the sentiment result.(Looking bad I know and I will improve it later).
The user can be anyone who want to do the analysis to other's twitter. The basic user stories is what I said about Donald J. Trump.You can also use this analyzer to analyze anyone you want as long as the user is exist. Click the 'Sentiment analyze' button to show the result. It will tells you how this user recent sentiment.It can even analyze the user's retweet message and his/her opinion about the retweeted message if he/she said something about it. I will do the hashtag search and sentiment analysis if time permitted since the API keeps return status code 429 and I don't know how to solve it now. 
To understand the result,the score shows the sentiment range from -1 to 1. The magnitude shows the overall sentiment from 0 to +inf. Here is some samples about how to read the score and magnitude

| Sentiment         | Sample Values                     | 
| :-------------    | :----------:                      | 
| Clearly Positive  | "score": 0.8, "magnitude": 3.0    | 
| Clearly Negative  | "score": -0.6, "magnitude": 4.0   | 
| Neutral           | "score": 0.1, "magnitude": 0.0    | 
| Mixed             | "score": 0.0, "magnitude": 4.0    | 
