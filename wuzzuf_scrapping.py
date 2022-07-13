#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
scr=result.content
soup=BeautifulSoup(scr,"lxml")
titels=soup.find_all("h2",{"class":"css-m604qf"})
company_name=soup.find_all("div",{"class":"css-d7j1kk"})
location=soup.find_all("span",{"class":"css-5wys0k"})
skills=soup.find_all("div",{"class":"css-y4udm8"})
job_titels=[]
company=[]
loc=[]
skill=[]
links=[]
salary=[]
for i in range(len(titles)):
    job_titels.append(titels[i].text)
    links.append(titels[i].find("a").attrs['href'])
    company.append(company_name[i].text)
    loc.append(location[i].text)
    skill.append(skills[i].text)

for link in links:
    result2=requests.get(link)
    scr2=result2.content
    soup=BeautifulSoup(scr2,"lxml")
    salaries=soup.find("span",{"class":"css-4xky9y"})
    salary.append(salaries.text)
    
file_list=[job_titels,company,loc,skill,links,salary]
#unpacking
ex=zip_longest(*file_list)
with open('wuzzuf_scrapping.csv', 'w') as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["Jop Title","Company Name","Location","Skills","links","salary"])
    wr.writerows(ex)


# In[ ]:





# In[ ]:




