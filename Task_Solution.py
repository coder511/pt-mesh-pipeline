#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
url ="https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid"


# In[2]:


import datetime


# In[3]:


# STEP-1: GET THE HTML

r = requests.get(url)   # r variable has all the HTML code
htmlContent = r.content # r returns response so if we want the code we write r.content
htmlContent = str(htmlContent)
print(len(htmlContent))


# In[4]:


# STEP-2: PARSE THE HTML
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
print(type(soup))


# In[5]:



#print(soup.prettify[:500]()) # to print html in tree structure


# In[6]:


#get title of html page
title=soup.title
print(title)
print(type(title))


# In[7]:


with open('webpage.html', 'w', encoding='utf-8') as f:
    f.write(htmlContent)


# In[8]:


#Get all the paragraphs from the page
paras=soup.find_all("p")
print(paras)


# In[9]:


#Get all the anchor tags from the page
anchors=soup.find_all("a")
print(len(anchors))


# In[10]:


all_links=set()
#Get all the links on the page
for link in anchors:
    if (link.get('href')!='#'):
        linkText="https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid"+link.get('href')
        all_links.add(link)
        print (linkText)


# In[11]:


heading_tags=soup.find_all('th')
heading_tags


# In[12]:


data_table=soup.find('table', class_="table")


# In[13]:


print(data_table)


# In[14]:


data=[]
for event_id in data_table.find_all('tbody'):
    rows = event_id.find_all('tr')
    for row in rows:
        id_id=row.find_all(('td'))
        data.append(id_id)      


# In[15]:


data[0]


# In[16]:


data[0][0].find_all('a')[0]
urls=[]
statement=[]
dates=[]
ind=-1
ind1=-1
for i in range(0,len(data)):
    ind=str(data[i][2]).index('T')
    ind1=str(data[i][1])[4::].index('<')
    urls.append(data[i][0].find_all('a')[0].text)
    statement.append(str(data[i][1])[4:ind1])
    dates.append(str(data[i][2])[4:ind])


# In[17]:


urls,dates,statement


# In[18]:


type(urls)


# In[19]:


import pandas as pd


# In[20]:


pandas_table={
    'Event ID': urls,
    'Event Name': statement,
    'End Date': dates
}


# In[21]:


len(urls)


# In[22]:


len(statement)


# In[23]:


len(dates)


# In[24]:


pandas_table


# In[25]:


OUR_TABLE=pd.DataFrame(pandas_table)


# In[26]:


OUR_TABLE


# In[29]:


OUR_TABLE.to_csv('output.csv', index=False)


# In[ ]:





# In[ ]:




