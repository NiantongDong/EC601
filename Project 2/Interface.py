import PySimpleGUI as sg
import TweetAPI as mine
import GoogleNLP as GNLP

sg.theme('DarkTanBlue')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter the person you want to search')],
            [sg.Text('User name:'), sg.InputText()],
            [sg.Text('Number of tweets you want'),sg.InputText()],
            [sg.Button('Search Tweet'),sg.Button('Sentiment analyze')], sg.Button('Quit')]


# Create the Window
window = sg.Window('Tweets Hashtag sentiment analyzer', layout)

# Set up Twitter authorization
Tweet_api = mine.Authorization_Setup()



# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':	# if user closes window or clicks cancel
        break

    User_tweets_result = mine.Get_User_Timeline(Tweet_api,values[0],values[1])
    User_tweets_result_Text = mine.Display_tweets(User_tweets_result)
    if event == 'Search Tweet':
        sg.popup('Twitter text:',User_tweets_result_Text)
    if event == 'Sentiment analyze':
        Sentiment_result = GNLP.Analyze(User_tweets_result_Text)
        sg.popup('Sentiment score',Sentiment_result)
window.close()