import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
consumer_key = "zSHk5JJKYBW0ttPwvzfpEDvfq"
consumer_secret = "M91khDhMZNDa2VcHlZKvaCRUUKv9UN4xVLHGxNpaU0YAlSNm6M"
access_key = "1210230929941303297-TOIES5xSbqIHIrotWPpJYjgyOqDHbg"
access_secret = "2Q9SZ1NrGZwfDUDJVDnMjK106v62fkVvjkpiaV2UkzJDv"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
tweepy.debug(True)
csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = "AI"      # enter your words
new_search = search_words + " -filter:retweets"
 
for tweet in tweepy.Cursor(api.search,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
