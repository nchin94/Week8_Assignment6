#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


location = 'C:\\Users\\nchin\\DataViz\\Week8_files\\gradedata.csv'


# In[4]:


df = pd.read_csv(location)


# In[8]:


df = df.sort_values(by=['lname', 'age', 'grade'], ascending=[True, True, True]) 


# In[9]:


df

