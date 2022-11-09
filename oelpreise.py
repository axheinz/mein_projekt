#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel('https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls', sheet_name="Data 1",skiprows=2)


# In[4]:


df


# In[5]:


df.columns = ['Datum', 'Dollars pro Barrel']


# In[6]:


df


# In[7]:


df.info() # Wird die Datumspalte als Datum erklannt? 


# In[8]:


df = df.set_index('Datum')


# In[9]:


df_resampled = df.resample('M').mean() #wir berechnen den monatlichen Durchshcnitt 


# In[10]:


df_resampled


# In[11]:


# df_resampled.plot.line()


# In[12]:


df_resampled.to_csv('oelpreise.csv')


# In[ ]:




