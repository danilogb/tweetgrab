import sqlite3
import json

def create_connection():
    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    c.execute('''
                CREATE TABLE IF NOT EXISTS tweets
                (tweet_id INTEGER PRIMARY KEY, 
                text TEXT,
                created_at TIMESTAMP,
                location TEXT,
                user_id INTEGER,
                username TEXT,
                mentions TEXT)
                ''')
    return conn


def insert_tweet(conn, tweet):
    # retrieving data from tweet object
    tweet_id = tweet.id
    text = tweet.text
    created_at = tweet.created_at
    location = json.dumps(tweet.coordinates)
    user_id = tweet.user.id
    username = tweet.user.screen_name
    mentions = json.dumps(tweet.entities['user_mentions'])
    
    # inserting data into database
    c = conn.cursor()
    c.execute("INSERT INTO tweets (tweet_id, text, created_at, location, user_id, username, mentions) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                (tweet_id, text, created_at, location, user_id, username, mentions))
    conn.commit()