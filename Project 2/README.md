# Project 2
Reference :
For TweetAPI.py, Most of codes are modified based on the offical tweepy tutorial.
For GoogleNLP.py, Modified from offical Google NLP tutorial.

Python GUI Programming With Tkinter:https://realpython.com/python-gui-tkinter/#:~:text=Python%20has%20a%20lot%20of,Windows%2C%20macOS%2C%20and%20Linux.&text=Although%20Tkinter%20is%20considered%20the,framework%2C%20it's%20not%20without%20criticism.
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