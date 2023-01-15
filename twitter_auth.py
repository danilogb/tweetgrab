import tweepy
import json

def authenticate():
    """Authenticates connection with Twitter API via Tweepy module. 
    Required to have a 'credentials.json' file in the same directory 
    containing user access information.

    Returns:
        object: tweepy API connection
    """
    # Opening JSON file
    with open('credentials.json') as f:
        credentials = json.load(f)
        consumer_key = credentials['consumer_key']
        consumer_secret = credentials['consumer_secret']
        access_token = credentials['access_token']
        access_token_secret = credentials['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)