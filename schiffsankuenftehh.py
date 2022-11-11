#!/usr/bin/env python
# coding: utf-8

# In[146]:


import pandas as pd
import requests
import json
import os


# In[1]:


token = os.environ ['MSTEAMS']


# In[113]:


url='https://coast.hhla.de/api/execute-report/Standard-Report-Segelliste'


# In[114]:


r = requests.get(url)


# data = r.json()
# pd.DataFrame(data)

# In[115]:


data = json.loads(r.text) # wandelt den Text des Abruf in eine gültige json datrei um 


# In[116]:


pd.json_normalize(data['resultTables'][0]['rows'][0])


# In[ ]:





# In[117]:


zeilen = data ['resultTables'][0]['totalNumberOfRows']


# In[118]:


df_liste = []


# In[ ]:





# In[119]:


for id in range(0,zeilen):
    einzel_df = pd.json_normalize(data['resultTables'][0]['rows'][id]).T
    einzel_df.columns = einzel_df.iloc[0]
    einzel_df = einzel_df[1:]
    df_liste.append(einzel_df)


# In[120]:


df_komplett = pd.concat (df_liste)


# In[121]:


df_komplett


# In[122]:


df_komplett.sort_values(by='schiffabfertigung.ankunftsollzeitpunkt', inplace=True)


# In[123]:


df_komplett = df_komplett.reset_index()


# In[124]:


df_komplett


# In[125]:


df_komplett['schiffabfertigung.schiffstyp'].value_counts()


# In[126]:


df_komplett['schiffabfertigung.ankunftsollzeitpunkt'] = pd.to_datetime(df_komplett['schiffabfertigung.ankunftsollzeitpunkt'])


# In[128]:


df_deepsea


# In[127]:


df_deepsea = df_komplett[df_komplett['schiffabfertigung.schiffstyp']== 'DEEPSEA']


# In[129]:


import datetime


# In[130]:


import pytz


# In[131]:


utc=pytz.UTC


# In[132]:


heute = utc.localize(datetime.datetime.now())


# In[133]:


df_deepsea[df_deepsea['schiffabfertigung.ankunftsollzeitpunkt'] > heute]


# In[134]:


df_deepsea_abheute = df_deepsea[df_deepsea['schiffabfertigung.ankunftsollzeitpunkt'] > heute]


# In[140]:


new_str = [str(x) for x in df_deepsea_abheute15['schiffabfertigung.schiffsname']]
new_str


# In[142]:


get_ipython().system('pip install pymsteams')


# In[143]:


import pymsteams


# In[144]:


text = ', '.join(new_str) # macht aus einer Liste einen String


# In[145]:


myTeamsMessage = pymsteams.connectorcard(token)
myTeamsMessage.text(text)
myTeamsMessage.send()

