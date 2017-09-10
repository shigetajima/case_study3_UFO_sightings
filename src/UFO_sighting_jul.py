
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
from itertools import izip
import pandas as pd


# In[2]:

url_Jul = "http://www.nuforc.org/webreports/ndxe201707.html"


# In[3]:

content_jul = requests.get(url_Jul)


# In[4]:

soup_jul = BeautifulSoup(content_jul.text, "html.parser")


# In[5]:

soup_jul.prettify()


# In[6]:

date_time_jul=[]
for link in soup_jul.find_all('a'):
    date_time_jul.append(str(link.get_text()))
    
date_time_jul = date_time_jul[1:]
date_jul, time_jul, time_jul_int =[], [], []
for d in date_time_jul:
    date_jul.append(d[0:7])
    time_jul.append(d[7:])

time_jul = [(x.strip().split(":"))[0] for x in time_jul]
for t in time_jul:
    if t == "":
        continue
    time_jul_int.append(int(t))

print time_jul_int


# In[7]:

len(soup_jul.find_all("font"))


# In[8]:

soup_jul.findAll('font')[14].next


# In[9]:

shape_jul=[]

for i in xrange(14,len(soup_jul.find_all("font")), 7):
    shape_jul.append(str(soup_jul.findAll('font')[i].next))


# In[10]:

shape_jul


# In[11]:

soup_jul.findAll('font')[13].next


# In[12]:

states_jul=[]
for i in xrange(13,len(soup_jul.find_all("font")), 7):
    states_jul.append(str(soup_jul.findAll('font')[i].next))
    
states_jul = states_jul[1:]

print states_jul



# In[13]:

state_shape_date_jul = [x for x in izip(date_jul,time_jul_int,states_jul,shape_jul)]
print state_shape_date_jul


# In[14]:

state_shape_date_sorted_jul = sorted(state_shape_date_jul, key = lambda x: x[2])
state_shape_date_sorted_jul = state_shape_date_sorted_jul[6:] 
state_shape_date_sorted_jul[0]


# In[17]:

df_jul = pd.DataFrame(state_shape_date_sorted_jul, columns =["Date", "Time", "State", "Shape"])
df_jul.head(10)


# In[16]:

df_jul.groupby("State").count()


# In[ ]:



