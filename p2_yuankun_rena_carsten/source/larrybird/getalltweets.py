# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:56:56 2013

"""


def getAllTweets(api, screen_name):
    """Return all tweets for a given screenname.
    
    :param api: the api instance of tweepy api class.
    :type api: tweepy.API.
    :param screen_name: The screen name of twitter.
    :type screen_name: String
    :returns:  A List full of  all tweets of this given screenname. 
    """
    # initialize a list to hold all the tweepy Tweets
    alltweets = []	
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    # save the newest 200 tweets
    alltweets.extend( new_tweets )
    # get the oldest tweet's ID
    oldID = alltweets[-1].id - 1
    # use this information to get other tweets
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldID)
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldID)
        #save most recent tweets
        alltweets.extend(new_tweets)
        #update the id of the oldest tweet less on
        oldID = alltweets[-1].id - 1
        print "...%s tweets downloaded so far" % (len(alltweets))
    saveTweets(alltweets)
    return alltweets

def saveTweets(alltweets):
    """Save all given tweets to two local file.
    One is a raw file, that stores the orginal data from api.
    The other one is a refined file for using.
    Both file use the user's screen_name als filename.
    Extention is .db.
    Attention: Both files are stored in data directory
    
    :param alltweets: a List of all retrievaled tweets
    :type alltweets: List
    :returns: True if successful, False if not
    """
    # get the user's screen_name
    screen_name = alltweets[0].user.screen_name
    # get the current file dir
    #import os
    #dirname = os.path.dirname(__file__) + "/data/"
    # first store the raw data with pickle module
    import pickle
    with open("data/" + screen_name + "_raw.db", "wb") as f:
        pickle.dump(alltweets, f )
        print("%_raw.db data was stored")
    # extract what we want from alltwees, then store this information 
    usefull = extractUsefulInfo(alltweets)
    with open("data/"+ screen_name + ".db", "wb") as f:
        pickle.dump(usefull, f)
        print("%.db data was stored")
 
def extractUsefulInfo(alltweets):
    """Extra usefull Information for our project.
    Such like created time, hashtags, source(client), text
    Erery Item hast a tweet_id as key,
    a tuple consists of (text, hashtags, source, created_at)
    
    
    :param alltweets: a List of all retrievaled tweets
    :type alltweets: List
    :returns: a List full of usefull infomation as Tuple
    """
    results = []
    for s in alltweets:
        if s.id :
            t_id = s.id
            t_text = s.text
            t_hashtags = [ent['text'] for ent in s.entities['hashtags']]
            t_created_at = s.created_at            
            t_source = s.source
            results.append((t_id,t_text, t_hashtags,
                             t_created_at, t_source))
        else:
            continue
    return results
                
                
 
    
