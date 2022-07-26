#!/usr/bin/env python
# coding: utf-8

# # Open up a Jupyter notebook!!!!
# 
# We're going to write a scraper!!!!

# In[21]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[7]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text)


# In[15]:


# Grab all of the titles
titles = doc.select(".media__title a")
titles


# In[18]:


for title in titles:
    # title
    print(title.text.strip())
    # link
    print(title['href'])


# In[22]:


# Start with an empty list
rows = []

for title in titles:
    # Go through each title, building a dictionary
    # with a 'title' and a 'url'
    row = {}
    
    # title
    row['title'] = title.text.strip()
    # link
    row['url'] = title['href']
    
    # Then add it to our list of rows
    rows.append(row)

# then we're going to make a dataframe from it!!!
df = pd.DataFrame(rows)
df.head()


# In[23]:


df.to_csv("bbc.csv", index=False)


# In[ ]:




