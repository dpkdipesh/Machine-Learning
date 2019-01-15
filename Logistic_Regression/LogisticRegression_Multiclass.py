#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression: Multiclass Classification

# In[3]:


from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


# In[4]:


load_iris


# In[7]:


iris=load_iris()


# In[9]:


dir(iris)


# In[11]:


iris


# target_names': array(['setosa', 'versicolor', 'virginica']
# 
# 
# feature_names': ['sepal length (cm)',
#   'sepal width (cm)',
#   'petal length (cm)',
#   'petal width (cm)']

# In[22]:


iris.target[7]


# In[14]:


from sklearn.linear_model import LogisticRegression


# In[15]:


lreg=LogisticRegression()


# In[17]:


from sklearn.model_selection import train_test_split


# In[23]:


X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.3)


# In[25]:


lreg.fit(X_train,y_train)


# In[27]:


lreg.predict(iris.data[0:20])


# In[29]:


lreg.score(X_test,y_test)


# In[ ]:





# In[ ]:




