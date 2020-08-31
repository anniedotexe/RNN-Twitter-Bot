model_dir = 'model/'
weights = '_weights.hdf5'
vocab = '_vocab.json'
config = '_config.json'

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Make adjustments below with your model file names and to tweak values for your twitter bot

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Name of the model used for the weights and configuration files you downloaded from Colaboratory
model_name = 'dickinson'

# Higher temperature will generate crazier text
# Recommended to be between 0.7 and 1.0
# You can also make it a temperature schedule (list) to cycle through
#   i.e. [1.0, 0.7, 0.2, 0.2] will give you 1 very unexpected token, 1 unexpected token, 2 expected tokens, and repeat
temperature = 0.7

# Set a prefix if you want each generated text to start with a given seed text
prefix = None

# Number of texts to generate
n = 1

# Maximum number of characters for each text generated
max_gen_length = 1000

# Set the max number of characters for each tweet to have
# Twitter's character limit for a tweet is 280
# The generated text is separated by new lines, 
#   so if some text is too long to fit into one tweet, 
#   it will be split into multiple tweets at this length
max_tweet_length = 260

# Optional if you want to add text to end of tweets
#   - Set to None if you do not want to use
add_to_tweet = '\n#EmilyDickinson'

# Time to wait in between each tweet in seconds
delay = 3600

# Minumum number of characters in the tweet
# Since the generated text is separated by new lines, sometimes we get really short tweets and want to skip over them
#   - Set to 0 if the above statement is not relevent to you
min_tweet_length = 50
