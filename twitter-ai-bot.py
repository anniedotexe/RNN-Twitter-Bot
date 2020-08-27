import tweepy
import logging
from textgenrnn import textgenrnn
from time import sleep
from random import randrange
from credentials import *
from config import *

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

def create_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Authentication Error', exc_info=True)
        raise e
    logger.info(f"Authentication OK. Connected to @{api.me().screen_name}")

    return api

def tweet_from_generated_text(api):

    
    while True: 
        textgen = textgenrnn(weights_path=model_dir+weights,
                            vocab_path=model_dir+vocab,
                            config_path=model_dir+config)

        logger.info(f'Generating text to {gen_file} ...')
        textgen.generate_to_file(gen_file, 
                                temperature=temperature, 
                                prefix=prefix, 
                                n=n,
                                max_gen_length=max_gen_length,
                                )

        with open(gen_file, "r", encoding="UTF-8") as in_file:        
            tweets = in_file.read()[1:].split("\n\n")

        while len(tweets) > 1:
            # Get a random tweet
            index = randrange(0, len(tweets))
            tweet = tweets.pop(index) 

            # Skip tweet if it is too short
            if len(tweet) > min_tweet_length:
                # Split into multiple tweets if too long
                if len(tweet) > max_tweet_length:
                    tweet_trimmed = [tweet[i:i+max_tweet_length] for i in range(0, len(tweet), max_tweet_length)]
                    for tw in tweet_trimmed:
                        # Skip tweet if it is too short
                        if len(tw) > min_tweet_length:
                            tw += add_to_tweet 
                            logger.info(f'Tweeting: \n{tw}\n')
                            api.update_status(status=tw)
                            sleep(delay)
                else:
                    tweet += add_to_tweet
                    logger.info(f'Tweeting: \n{tweet}\n')
                    api.update_status(status=tweet)
                    sleep(delay) 

if __name__ == "__main__":
    api = create_api()
    tweet_from_generated_text(api)
