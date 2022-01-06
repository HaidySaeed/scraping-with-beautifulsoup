#!/usr/bin/env python
# coding: utf-8

# In[45]:


import requests
import csv
from bs4 import BeautifulSoup
import pytube  
from pytube import YouTube  
source=requests.get("https://coreyms.com/").text
soup=BeautifulSoup(source,"lxml")


# In[35]:


links=[]
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('WebScrap.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    

    summary = article.find('div', class_='entry-content').p.text
    

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
        
    #print(yt_link)
    links.append(yt_link)
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()


# In[44]:




