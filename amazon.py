#!/usr/bin/env python
# coding: utf-8

# In[130]:


import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup as bs


# In[131]:


kindle=[]


# In[135]:



for i in range(1,5):
    url="https://www.amazon.in/Einstein-Box-Girls-Learning-Educational/product-reviews/B01MQISR84/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=i"
    response=requests.get(url)
    soup = bs(response.content,"html.parser")
    reviews=soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"}
    )


# In[ ]:


for i in range(1,5):
    url="https://www.amazon.in/All-New-Kindle-reader-Glare-Free-Touchscreen/product-reviews/B0186FF45G/ref=cm_cr_getr_d_paging_btm_3?showViewpoints=1&pageNumber=i"
    response=requests.get(url)
    soup = bs(response.content,"html.parser")
    reviews=soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"}
    )


# In[143]:


kindle_review=[]
for i in range(len(reviews)):
    kindle_review.append(reviews[i].text)


# In[138]:


kindle_review


# In[150]:


kindle_review=" ".join(kindle_review)


# In[151]:


kindle_review


# In[53]:


import re


# In[146]:


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


# In[152]:


kindle_review=clean_text(kindle_review)


# In[154]:


kindle_review


# In[155]:


from wordcloud import WordCloud
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')


# In[156]:


kindle_review=word_tokenize(kindle_review)


# In[69]:


stopwords1=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves','was' ,'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',  'nor',  'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't",  'ma',  'shan'] 


# In[157]:


kindlereviews=[]
for i in kindle_review:
    if i not in stopwords1:
        kindlereviews.append(i)
 


# In[92]:


#kindlereviews=" ".join(kindlereviews)


# In[114]:


wordcloud_ip = WordCloud(
                      background_color='black',
                      width=2000,
                      height=1600
                     ).generate(kindlereviews)


# In[101]:


plt.imshow(wordcloud_ip)


# In[103]:


with open("A:/Data Science/assignments/Text mining/negative-words (1).txt", 'r') as neg:
    negwords=neg.read()
with open("A:/Data Science/assignments/Text mining/positive-words (1).txt", 'r') as pos:
   poswords=pos.read()


# In[117]:


negative=[]
for i in kindlereviews:
    if i in negwords:
        negative.append(i)


# In[119]:


negative=" ".join(negative)


# In[120]:


negative


# In[121]:


wordcloud_neg = WordCloud(
                      background_color='black',
                      width=2000,
                      height=1600
                     ).generate(negative)


# In[122]:


plt.imshow(wordcloud_neg)


# In[126]:


poistive=[]
for i in kindlereviews:
    if i in poswords:
        poistive.append(i)


# In[127]:


poistive=" ".join(poistive)
poistive


# In[128]:


wordcloud_pos = WordCloud(
                      background_color='black',
                      width=2000,
                      height=1600
                     ).generate(poistive)


# In[129]:


plt.imshow(wordcloud_pos)


# In[ ]:




