import argparse
import os
import sys

import tweepy
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="display userId" )
parser.add_argument("--count", help="Number of twitts")
args = parser.parse_args()

rootPath = "/home/swapnil"
os.chdir(rootPath)

with open('test.yml', 'r') as ymlfile:
    doc = yaml.load(ymlfile)
    
consumerKey = doc["CONSUMER_KEY"]
consumerSecret = doc["CONSUMER_SECRET"]
accessToken = doc["ACCESS_TOKEN"]
accessTokenSecret = doc["ACCESS_TOKEN_SECRET"]

if not os.path.exists('user_logs'):
    os.mkdir('user_logs')

os.chdir( rootPath + '/user_logs')

if not os.path.exists(args.name):
    os.mkdir(args.name)

os.chdir( rootPath + '/user_logs/' + args.name)

auth = tweepy.OAuthHandler( consumerKey, 
                            consumerSecret)

auth.set_access_token(accessToken,
                      accessTokenSecret)

api = tweepy.API(auth)

user_tweets = api.user_timeline(args.name , count =  args.count)

for tweet in user_tweets:
    with open(str(tweet.created_at), 'w+') as fileName:
        fileName.write(tweet.text.encode('utf-8'))        
