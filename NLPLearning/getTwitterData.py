import tweepy
import pandas as pd

api_key = "SnxucIPt1fg7UUyVOT0T5j0pR"
api_key_secret = "yaToQPv95OA1fiNTHD8drKM8g8rZGM7jSQnPOLoxU3QA9UpaLm"
access_token = "1722424471-Xb0DjPVOqXsLj2sXEYXmU2sqxaDC4B793erGO6J"
access_token_secret = "D2LyXN11zAoZB0M476eb1ZGDM55oRvy4tBWNb8pR4CO0h"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAADnkgEAAAAAgEkTccGImU4WtBjMxyMszSdpswg%3DAFjvso7ju8wFAv1G6cWM2xnOud9F0FaxjHnwpfLbwtXd9Swlxc"
auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

query = "คริสต์มาส"

df = pd.DataFrame(columns= ["text","hashtag"])
print(df.columns)

count = 0
for tweet in tweepy.Cursor(api.search_tweets,q=query,count=100,
result_type="recent",tweet_mode='extended').items():
    entity_hashtag = tweet.entities.get('hashtags')
    hashtag = ""
    for i in range(0,len(entity_hashtag)):
        hashtag = hashtag +"/"+entity_hashtag[i]["text"]
    try:
        text = tweet.retweeted_status.full_text
    except:
        text = tweet.full_text
    new_data = pd.Series([text,hashtag],index=df.columns)
    df = pd.concat([df,pd.DataFrame(new_data).T],ignore_index=True)
    count += 1
    print(f"Pulled Tweets : {count} tweets")
    if count == 15000:
        print("done")
        break
df.to_excel("twitterCrawler.xlsx")