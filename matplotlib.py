#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[15]:


#load the dataset
data1=pd.read_csv('D:/bindu/dataanalytics/gapminder_full.csv')


# In[17]:


data1


# In[21]:


#display the head of the dataset(shows only 5 rows)
data1.head()


# In[22]:


#get number of rows and columns
print(data1.shape)


# In[23]:


#get column names
data1.columns


# In[24]:


#get thhe data type of each column
data1.dtypes


# In[25]:


#get more information about data
data1.info()


# In[27]:


#looking at columns,rows and cells
# get the country column and save it n a new variable
country_data=data1['country']
#show the first 5 observation
country_data.head()


# In[28]:


#show the last 5 observation
country_data.tail()


# In[29]:


#looking at country, continent and year
subset=data1[['country','continent','year']]
subset.head()


# In[30]:


subset.tail()


# In[31]:


#analytical summary of the dataset
data1.describe(include='all')


# In[32]:


#histagram of all the variables in the dataset
data1.hist(figsize=(10,5))


# In[35]:


#relaionship between cataogrical and continious variable
sns.boxplot(x="year",y="life_exp",data=data1)


# In[36]:


#drop irrelevant columns
data1=data1.drop(['year'],axis='columns')
data1.head(5)


# In[37]:


#remaining the column name
data1=data1.rename(columns={"country" : "countries"})
data1.head(5)


# In[38]:


#rows containing dupliacte data
duplicate_rows=data1[data1.duplicated()]
print('NUmber of duplicate rows:',duplicate_rows.shape)


# In[39]:


#count the rows before moving data
data1.count()


# In[ ]:




