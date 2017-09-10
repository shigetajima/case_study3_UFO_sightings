
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
from itertools import izip
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[2]:

url_Jul = "http://www.nuforc.org/webreports/ndxevent.html"


# In[3]:

content_jul = requests.get(url_Jul)


# In[4]:

soup_jul = BeautifulSoup(content_jul.text, "html.parser")


# In[5]:

soup_jul.prettify()


# In[6]:

month=[]
for link in soup_jul.find_all('a'):
    month.append(str(link.get_text()))

month = month[1:]



# In[7]:

len(soup_jul.find_all("font"))


# In[8]:

soup_jul.findAll('font')[7].next


# In[9]:

count=[]

for i in xrange(7,len(soup_jul.find_all("font")), 2):
    count.append(int(soup_jul.findAll('font')[i].next))


# In[10]:

count


# In[11]:

month_count = [x for x in izip(month,count)]
print month_count


# In[20]:

df_mon = pd.DataFrame(month_count[:91], columns =["month_year","count"])
sns.barplot("month_year", "count", df_mon)
plt.show()
#datetime.strptime(df_mon"month_year", '%Y-%m-%d')



# In[25]:

df_mon.sort_values("count", ascending = False, inplace =True)

df_mon.head(24)


# In[ ]:




# In[ ]:
