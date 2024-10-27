# Author: Himarsha R. Jayanetti 
# Description: Script to collect data from X using Selenium
# Built using https://github.com/Prateek93a/selenium-twitter-bot/tree/master

import twitterbot as tb
import secrets, sys
 
# fetches the hashtag from command line argument
hashtag = sys.argv[1]
# fetches the credentials dictionary
# using get_credentials function
credentials = secrets.get_credentials()
# initialize the bot with your credentials
bot = tb.Twitterbot(credentials['email'], credentials['password'])
# logging in
bot.login(hashtag)
# calling like_retweet function
# bot.like_retweet(hashtag)
