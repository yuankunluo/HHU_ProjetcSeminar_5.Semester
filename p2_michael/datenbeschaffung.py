import tweepy
import csv

#

consumer_key = "tFEI5cnie3R85Lf8ks3Zw"
consumer_secret = "i2tjjnM1p0Al3c63hq8OfKw1I1P1WCFVYE85ouyPkao"
access_token = "2190517982-5iS97fZtFMop8y2pf18WFBUPYPCJvfycIK3MBjB"
access_token_secret= "1zGQOBxrt9iZmgNhlUb1adt2xWyFPuVNX1T4JLbFZooS0"



# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

        

with open('rihanna.csv', 'wb') as csvfile:
    i = 0
    for page in tweepy.Cursor(api.user_timeline, count=200, id="rihanna", include_rts=True, include_entities = True, exclude_replies = False).pages(16):
        for tweet in page:
            csvwriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            alte_id = tweet.id_str
            # add hashtags
            hashtags = [ent['text'] for ent in tweet.entities['hashtags']]
            hashtags = " ".join(hashtags)
            csvwriter.writerow([tweet.text.encode('utf-8'),
                       tweet.source,
                       tweet.created_at,
                       tweet.author.name,
                       hashtags])
        print("get tweets %s"%(i*200 + 200))
        i += 1
            
print("data speichert!")

