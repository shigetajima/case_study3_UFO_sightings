
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
from itertools import izip
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[2]:

url_Jan = "http://www.nuforc.org/webreports/ndxe201701.html"


# In[3]:

content_jan = requests.get(url_Jan)


# In[4]:

soup_jan = BeautifulSoup(content_jan.text, "html.parser")


# In[5]:

soup_jan.prettify()


# In[6]:

date_time_jan=[]
for link in soup_jan.find_all('a'):
    date_time_jan.append(str(link.get_text()))
    
date_time_jan = date_time_jan[1:]
date_jan, time_jan, time_jan_int =[], [], []
for d in date_time_jan:
    date_jan.append(d[0:7])
    time_jan.append(d[7:])

time_jan = [(x.strip().split(":"))[0] for x in time_jan]
for t in time_jan:
    if t == "":
        continue
    time_jan_int.append(int(t))

print time_jan_int


# In[7]:

len(soup_jan.find_all("font"))


# In[8]:

soup_jan.findAll('font')[14].next


# In[9]:

shape_jan=[]

for i in xrange(14,len(soup_jan.find_all("font")), 7):
    shape_jan.append(str(soup_jan.findAll('font')[i].next))


# In[10]:

shape_jan


# In[11]:

soup_jan.findAll('font')[13].next


# In[12]:

states_jan=[]
for i in xrange(13,len(soup_jan.find_all("font")), 7):
    states_jan.append(str(soup_jan.findAll('font')[i].next))
    
states_jan = states_jan[1:]

print states_jan



# In[13]:

state_shape_date_jan = [x for x in izip(date_jan,time_jan_int,states_jan,shape_jan)]
print state_shape_date_jan


# In[14]:

state_shape_date_sorted_jan = sorted(state_shape_date_jan, key = lambda x: x[2])
state_shape_date_sorted_jan = state_shape_date_sorted_jan[11:] 
state_shape_date_sorted_jan


# In[17]:

df_jan = pd.DataFrame(state_shape_date_sorted_jan, columns =["Date", "Time", "State", "Shape"])


# In[18]:

df_jan.head(10)


# In[19]:

df_jan.groupby("State").count()


# In[ ]:



