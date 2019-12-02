#!/usr/bin/env python
# coding: utf-8

# In[143]:


import pandas as pd
df=pd.read_excel("C:\\Users\\shubham_kumar\\Desktop\\cod.xlsx",header=[0,1],index_col=0)

df


# In[145]:


#Converts itin to Stack

df=df.stack()
df


# In[139]:


#Converts it into Level 0 Stack

df=df.stack(level=0)
df


# In[141]:


#Converts it into unstack

df.unstack()


# In[150]:


df2=pd.read_excel("C:\\Users\\shubham_kumar\\Desktop\\cod2.xlsx",header=[0,1,2],index_col=0)

df2


# In[159]:


df2.stack() #or df2.stack(level=2)


# In[158]:


df2.stack(level=1)

