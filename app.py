import twitter_auth
import db
import tweepy

def main(search_term):
    # Authenticate with Twitter API
    api = twitter_auth.authenticate()
    
    # Connect to SQLite database
    conn = db.create_connection()
    
    # Retrieve tweets
    for page in tweepy.Cursor(api.search_tweets, q=search_term, count=100).pages(100):
        for tweet in page:
            # Insert tweet into database
            db.insert_tweet(conn, tweet)
            
    # Close database connection
    conn.close()
    
    
if __name__ == '__main__':
    main(search_term= "Bolsonaro")
