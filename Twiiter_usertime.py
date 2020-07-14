#!/usr/bin/env python
# coding: utf-8

# In[343]:


import pandas as pd
import tweepy as twt
import twitter 


# In[ ]:


twitter.api


# In[394]:


# initialize api instance
consumer_key='ALG1czMmiKtwpv3rsnRzr5QQe'
consumer_secret='0P1TzaUVT2RvZfCNJpyOBbVDVayLsNRhjsX5BPjaRYlRL4Dj95'
access_key='1280017030603776001-mtmyVeDq3ituiPiXdNEc6s2jwvrGYx'
access_secret='HbSE6Yp8jmSlOkPaCYpHIatpUgvoIcjhRuIwRlFU2nmDJ'


# In[472]:


alltweets = []	

def get_all_tweets(screen_name):
    auth = twt.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = twt.API(auth)
    new_tweets = api.user_timeline(screen_name =screen_name,count=10)
    alltweets.extend(new_tweets)


# In[473]:


get_all_tweets('@realDonaldTrump')


# In[474]:


alltweets


# In[475]:


outtweets = [[tweet.created_at,tweet.entities["hashtags"],tweet.entities["user_mentions"],tweet.favorite_count,
                  tweet.geo,tweet.id_str,tweet.lang,tweet.place,tweet.retweet_count,tweet.retweeted,tweet.source,tweet.text,
                  tweet._json["user"]["location"],tweet._json["user"]["name"],tweet._json["user"]["time_zone"],
                  tweet._json["user"]["utc_offset"]] for tweet in alltweets]


# In[476]:


outtweets


# In[477]:


tweets_df = pd.DataFrame(columns = ["time","hashtags","user_mentions","favorite_count",
                                    "geo","id_str","lang","place","retweet_count","retweeted","source",
                                    "text","location","name","time_zone","utc_offset"])


# In[478]:


tweets_df


# In[479]:


tweets_df["time"]  = pd.Series([str(i[0]) for i in outtweets])
tweets_df["hashtags"] = pd.Series([str(i[1]) for i in outtweets])
tweets_df["user_mentions"] = pd.Series([str(i[2]) for i in outtweets])
tweets_df["favorite_count"] = pd.Series([str(i[3]) for i in outtweets])
tweets_df["geo"] = pd.Series([str(i[4]) for i in outtweets])
tweets_df["id_str"] = pd.Series([str(i[5]) for i in outtweets])
tweets_df["lang"] = pd.Series([str(i[6]) for i in outtweets])
tweets_df["place"] = pd.Series([str(i[7]) for i in outtweets])
tweets_df["retweet_count"] = pd.Series([str(i[8]) for i in outtweets])
tweets_df["retweeted"] = pd.Series([str(i[9]) for i in outtweets])
tweets_df["source"] = pd.Series([str(i[10]) for i in outtweets])
tweets_df["text"] = pd.Series([str(i[11]) for i in outtweets])
tweets_df["location"] = pd.Series([str(i[12]) for i in outtweets])
tweets_df["name"] = pd.Series([str(i[13]) for i in outtweets])
tweets_df["time_zone"] = pd.Series([str(i[14]) for i in outtweets])
tweets_df["utc_offset"] = pd.Series([str(i[15]) for i in outtweets])
tweets_df.to_csv('mohanlal'+"_tweets.csv")
#return tweets_df


# In[480]:


tweets_df


# In[481]:


text=tweets_df.text


# In[482]:


text


# In[483]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re


# In[484]:


tweets_1=tweets_df['text']


# In[485]:


tweets_1


# In[486]:


tweets_1=str(tweets_1)
tweets_1


# In[487]:


def clean_text(cleaned_text):
    cleaned_text=cleaned_text.lower()
    cleaned_text=re.sub("\n", " ",cleaned_text)
    cleaned_text=re.sub('((www\.[^\s]+)|(https?://[^\s]+))', " ", cleaned_text)
    cleaned_text=re.sub("[0-9" "]+"," ",cleaned_text)
    cleaned_text = re.sub('#', '', cleaned_text)
    cleaned_text= re.sub('RT[\s]+', '', cleaned_text)
    cleaned_text= re.sub('[^a-zA-Z0-9 \n\.]', '', cleaned_text)
    cleaned_text= re.sub('https?:\/\/\S+', '', cleaned_text)
    return cleaned_text


# In[488]:


cleaned_text=clean_text(tweets_1)
cleaned_text


# In[489]:


import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
cleaned_text=word_tokenize(cleaned_text)


# In[490]:


cleaned_text


# In[491]:


from nltk.corpus import stopwords
nltk.download('stopwords')


# In[492]:



print(stopwords.words('english'))


# In[493]:


stopwords1=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves','was' ,'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',  'nor',  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't",  'ma',  'shan'] 


# In[494]:


filtered_sentence = [] 
for w in cleaned_text: 
    if w not in stopwords1: 
        filtered_sentence.append(w) 


# In[495]:


filtered_sentence


# In[496]:


sentiment=" ".join(filtered_sentence)
sentiment


# In[497]:


from wordcloud import wordcloud
import matplotlib.pyplot as plt


# In[498]:


wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(sentiment)


# In[499]:


plt.imshow(wordcloud_ip)


# In[505]:


with open("A:/Data Science/assignments/Text mining/negative-words (1).txt", 'r') as neg:
    negwords=neg.read()


# In[506]:


negwords


# In[507]:


negcloud=[]
for word in filtered_sentence:
    if word in negwords:
        negcloud.append(word)


# In[508]:


negcloud


# In[513]:


negreview=" ".join(negcloud)
negreview


# In[516]:


wordcloud_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(negreview)


# In[517]:


plt.imshow(wordcloud_neg)


# In[520]:


with open("A:/Data Science/assignments/Text mining/positive-words (1).txt", 'r') as pos:
   poswords=pos.read()


# In[521]:


poswords


# In[522]:


poscloud=[]
for word in filtered_sentence:
    if word in poswords:
        poscloud.append(word)


# In[524]:


posreview=" ".join(poscloud)
posreview


# In[525]:


wordcloud_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(posreview)


# In[526]:


plt.imshow(wordcloud_pos)

