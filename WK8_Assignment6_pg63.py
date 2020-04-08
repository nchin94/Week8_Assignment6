#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


location = 'C:\\Users\\nchin\\DataViz\\Week8_files\\gradedata.csv'


# In[5]:


df = pd.read_csv(location)


# In[7]:


df.head()


# In[3]:


import statsmodels.formula.api as sm 


# In[13]:


result = sm.ols(formula='grade ~ age + exercise + hours', data=df).fit() 


# In[9]:


result.summary()


# In[10]:


def gender(x):
    if x == 'male':
        return 0
    if x == 'female':
        return 1


# In[15]:


df['m_f'] = df['gender'].apply(gender)


# In[16]:


df.head()


# In[17]:


result = sm.ols(formula='grade ~ exercise + hours + m_f', data=df).fit() 


# In[18]:


result.summary()

