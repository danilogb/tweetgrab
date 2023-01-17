import twitter_auth
import db
import tweepy
from tqdm import tqdm
from datetime import datetime, timedelta

def main(search_term, days_in_time):
    # now = datetime.now()
    # x_days_ago = now - timedelta(days=days_in_time)
    
    # # Convert datetime to string
    # since_date = x_days_ago.strftime("%Y-%m-%d")
    # until_date = now.strftime("%Y-%m-%d")
    
    # Authenticate with Twitter API
    api = twitter_auth.authenticate()
    
    # Connect to SQLite database
    conn = db.create_connection()
    
    # Retrieve tweets
    for page in tqdm(tweepy.Cursor(api.search_tweets, 
                                   q=search_term,
                                   count=100).pages(100), 
                    desc='Retrieving tweets:'):
        for tweet in page:
            # Insert tweet into database
            db.insert_tweet(conn, tweet)
            
    # Close database connection
    conn.close()
    
    
if __name__ == '__main__':
    main(search_term = "Bolsonaro",  # insert search term here
         days_in_time=30)  # how many days the search goes back in time
