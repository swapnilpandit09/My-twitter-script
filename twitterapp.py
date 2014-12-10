import argparse
import os
import sys
import tweepy
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="display userId" )
parser.add_argument("--count", help="Number of twitts")
args = parser.parse_args()

os.chdir('/home/swapnil')

with open('test.yml', 'r') as ymlfile:
    doc = yaml.load(ymlfile)
    
consumerKey = doc["Consumer_Key"]
consumerSecret = doc["Consumer_Secret"]
accessToken = doc["Access_Token"]
accessTokenSecret = doc["Access_Token_Secret"]

if not os.path.exists('user_logs'):
    os.mkdir('user_logs')

os.chdir( '/home/swapnil/user_logs')

if not os.path.exists(args.name):
    os.mkdir(args.name)

os.chdir( '/home/swapnil/user_logs/' + args.name)

auth = tweepy.OAuthHandler( consumerKey, 
                            consumerSecret)

auth.set_access_token(accessToken,
                     accessTokenSecret)

api = tweepy.API(auth)

user_tweets = api.user_timeline(args.name , count =  args.count)
for tweet in user_tweets:
    fileDescriptor = open(str(tweet.created_at) , 'w+')
    fileDescriptor.write(tweet.text.encode('utf-8'))
