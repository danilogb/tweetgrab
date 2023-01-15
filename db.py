import sqlite3
import json

def create_connection():
    """Creates a connection with database

    Returns:
        object: sqlite database connection object
    """
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
                mentions TEXT,
                hashtags TEXT)
                ''')
    return conn


def insert_tweet(conn, tweet):
    """Inserts tweet information into database

    Args:
        conn (object): database connection
        tweet (object): tweet object retrieved from Twitter
    """
    # retrieving data from tweet object
    tweet_id = tweet.id
    text = tweet.text
    created_at = tweet.created_at
    location = json.dumps(tweet.coordinates)
    user_id = tweet.user.id
    username = tweet.user.screen_name
    mentions = json.dumps(tweet.entities['user_mentions'])
    hashtags = json.dumps(tweet.entities['hashtags'])
    
    # inserting data into database
    c = conn.cursor()
    c.execute("INSERT INTO tweets (tweet_id, text, created_at, location, user_id, username, mentions, hashtags) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                (tweet_id, text, created_at, location, user_id, username, mentions, hashtags))
    conn.commit()