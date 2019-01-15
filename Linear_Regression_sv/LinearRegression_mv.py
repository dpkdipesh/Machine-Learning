#!/usr/bin/env python
# coding: utf-8

# # Linear Regression Multiple variable

# In[1]:


from sklearn import linear_model
import pandas as pd
import numpy as np


# In[64]:


df=pd.read_csv(r'C:\Users\Deepak Dipesh\Desktop\Python projects\Datasets\hiring.csv',delimiter='\t')


# In[65]:


df


# In[66]:


#Finding median of score column
score_median=df['test_score(out of 10)'].mean()


# In[67]:


# Filling median to missing value of score columns
import math
median_score=math.floor(df['test_score(out of 10)'].mean())
df['test_score(out of 10)']=df['test_score(out of 10)'].fillna(median_score)


# In[68]:


df


# In[69]:


df


# In[70]:


df['experience']=df['experience'].fillna(0)


# In[71]:


df


# In[72]:


# We can convert numbers in word to digit by installing package word2number
#import word2number as w2n
#w2n(thirty five)
# output 35
#not using in this code as not able to intall that


# In[73]:


reg=linear_model.LinearRegression()


# In[74]:


reg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])


# In[75]:


reg.predict([[2,9,6]])


# In[48]:


reg.predict([[12,10,10]])


# # verification of above prediction

# In[76]:


reg.coef_


# In[77]:


reg.intercept_


# In[79]:


#y=m1*exp +m2* testscore + m3*intevscore + b
2922.26901502*2+2221.30909959*9+2147.48256637*6+14992.651446693118


# In[ ]:




