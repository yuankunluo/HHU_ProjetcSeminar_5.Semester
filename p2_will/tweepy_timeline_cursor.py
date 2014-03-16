from tweepy import OAuthHandler
import tweepy
import sys
import csv
import itertools
from time import sleep

 
consumer_key="aVZ66HJuMoLp50ODZ7QZnQ"
consumer_secret="h0qjmTYvwjARGxektizsq4feHP0cir34sOrccARA"

access_token="395493737-VoSH6fbXtL4rCu77HSyhvm6yQge3hSf2PrMLBwOB"
access_token_secret="wGoSCwvsRqdQ8s2OhnRvOR9ZNSPwNZl5h1wIefVRcDQsT"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#########################################################

def collectTweets(username):
    tweets_list = get_tweets_list(username)
    tweepy_list_to_csv(tweets_list, str(username))
    print("Data sammeln fertig!")
    
    


def tweepy_object_to_dict(tweepy_object):
    return_dict = {}
    for key,value in tweepy_object.__getstate__().items():
        if isinstance(value,tweepy.models.User):
            return_dict[key] = value.__getstate__()
        else:
            return_dict[key] = value
    return return_dict

def tweepy_list_to_csv(tweepy_list,outfile_name):
    fields = ['text','id','retweeted','created_at','source', 'hashtags']
    with open(outfile_name+'.csv','w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(fields)
        for tweepy_object in tweepy_list:
            tweepy_object_dict = tweepy_object_to_dict(tweepy_object)
            # add hashtags
            hashtags = [ent['text'] for ent in tweepy_object.entities['hashtags']]
            outdict = []
            for field in fields[:-1]:
                try:
                    outdict.append(str(tweepy_object_dict[field].encode('utf-8')))
                except:
                    outdict.append(tweepy_object_dict[field])
            outdict.append(" ".join(hashtags))
            csvwriter.writerow(outdict)


def get_tweets_list(username):
    tweets = []
    for status in tweepy.Cursor(api.user_timeline, id = username).items():
        tweets.append(status)
    return tweets
