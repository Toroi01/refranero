import tweepy
from keys import *
from refranero import *

def create_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        raise e
    return api

api = create_api()

def tweet():
    refran = get_cool_refran()
    api.update_status(refran)
      
def main():
    tweet()      

if __name__ == "__main__":
    main()
