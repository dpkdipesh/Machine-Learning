#!/usr/bin/env python
# coding: utf-8

# # Linerar Regression Single Variable 

# In[57]:


from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[58]:


canada=pd.read_csv(r'C:\Users\Deepak Dipesh\Desktop\Python projects\Datasets\Linreg_sv.xls',encoding='Latin-1',delimiter='\t')


# In[59]:


canada.head()


# In[60]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(canada['year'],canada['income'])
plt.xlabel('Year')
plt.ylabel('Income(US$)')


# In[61]:


reg=linear_model.LinearRegression()


# In[62]:


reg.fit(canada[['year']],canada['income'])


# # Predicting below the income in year 2020

# In[63]:


reg.predict(2020)


# # Verifiying the above result with linear eq y=mx+b

# In[64]:


#this is m
reg.coef_


# In[65]:


# This is b
reg.intercept_


# In[67]:


828.46507522*2020-1632210.7578554575


# In[ ]:


#Above output is equals to predicted value

