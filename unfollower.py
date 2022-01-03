#   Tweetbot unfollower
#   by Tomislav Rozman
#   Usage:
#   1. Define the filter (number of followers and number of tweets), search for vars filter_followers and filter_tweets
#   2. Run the program
#   3. This followerbot will unfollow all friends that match filter: number of followers and number of tweets
#   If it hits the Twitter limits (too many requests), it will wait for 15 mins and resume

from colorama import init, deinit # color text
from colorama import Fore, Back, Style

import tweepy
import datetime
import time
import logging

#read twitter keys from the config file (tweerconfig.txt)
print("Reading config file with twitter keys...")
def get_pair(line): #transform string line to 2 vars: key & value
    key, sep, value = line.strip().partition("=")
    return key, value

with open("tweetconfig.txt") as config_file:    
    config_keys = dict(get_pair(line) for line in config_file) #read line from the file, convert it to key,value and insert it into dict

print("Done.")

logging.basicConfig(filename='unfollower.log', encoding='utf-8', level=logging.DEBUG)

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = str(config_keys["consumer_key"])
consumer_secret = str(config_keys["consumer_secret"])

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = str(config_keys["access_token"])
access_token_secret = str(config_keys["access_token_secret"])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print("Authenticating to twitter again...")
# Authenticate Twitter
my_screen_name=str
try:
    TweetAPI = tweepy.API(auth,wait_on_rate_limit=False)
    
    # If the authentication was successful, this should print the
    # screen name / username of the account
    my_screen_name=TweetAPI.verify_credentials().screen_name
    print("Twitter username:"+my_screen_name)
    print("Auth. successfull!")
except:
    print("Auth. was not successfull!")
    exit()
#end try auth

init() #init colorama for coloured text

#helper vars and counters

no_of_unfollows=0

#filter for unfollow:
filter_followers=35
filter_tweets=150

print("Getting friend list ...")
friends=[]

#friends=TweetAPI.get_friends(screen_name=my_screen_name,count=200)
friendcount=0
 
#user attribs:
#https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/user
print(Fore.WHITE)
#for f in friends:
try:
    friends=tweepy.Cursor(TweetAPI.get_friends).items()

except Exception as e:
        print("Error getting friends:")
        print(e)
        exit
print("Iterating through friend list...")
for attempt in range(10): #retry if hit limit
    try:

        for f in friends:
            if f.followers_count<filter_followers or f.statuses_count<filter_tweets: #filters defined above
                print(Fore.RED)
                #unfollow
                print("Unfollowing "+ f.screen_name+" at:"+str(datetime.datetime.now()))
                logging.info("Unfollowing "+ f.screen_name+" at:"+str(datetime.datetime.now()))
                try:
                    TweetAPI.destroy_friendship(screen_name=f.screen_name)
                    no_of_unfollows+=1
                except Exception as e:
                    print("Error unfollowing:")
                    print(e)
                else:
                    print("Unfollow ok!")
                    time.sleep(5)

            else:
                print(Fore.WHITE)
            print(str(friendcount)+" "+ f.screen_name+" "+f.location+", followers:"+str(f.followers_count)+", tweets:"+str(f.statuses_count))
            friendcount+=1
        #for iterate friends
    except Exception as e:
            print("Error getting friends, now waiting for 16 mins. Attempt "+str(attempt)+" at:"+str(datetime.datetime.now()))
            print(e)
            #exit()
            time.sleep(16*60) #wait for 16 mins to overcome the rate limit
            print("Waiting done, continuing..." +" at:"+str(datetime.datetime.now()))
    else:
        print("Attempt to unfollow was successful, continuing after 6 secs...")
        time.sleep(6)
        break
else:
    #we failed all attempts to save, exiting
    print("All attempts failed, exiting...")
    exit()
#for - retry

print("Unfollowed:"+str(no_of_unfollows)+" at:"+str(datetime.datetime.now()))
exit()

deinit() #stop coloured output