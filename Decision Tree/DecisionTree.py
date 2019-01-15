#!/usr/bin/env python
# coding: utf-8

# # Decision Tree

# In[1]:


import pandas as pd


# In[6]:


df=pd.read_csv(r'C:\Users\Deepak Dipesh\Desktop\Python projects\Datasets\titanic.csv')


# In[8]:


df.head()


# In[12]:


df=df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns')


# In[36]:


df.head()


# In[33]:


df['Age']=df['Age'].fillna(df['Age'].mean())


# In[44]:


df[:10]


# In[58]:


input=df[['Pclass','Sex','Age','Fare']]


# In[59]:


input.head()


# In[60]:


target=df['Survived']


# # Breaking Sex value in 0 and 1 as ML don't accept string,We can also use dummy variable

# In[61]:


from sklearn.preprocessing import LabelEncoder


# In[62]:


le_sex=LabelEncoder()


# In[65]:


input['Sex_n']=le_sex.fit_transform(input['Sex'])


# In[67]:


input.head()


# In[70]:


input=input.drop(['Sex'],axis='columns')


# In[71]:


input.head()


# In[72]:


from sklearn import tree


# In[73]:


Dte = tree.DecisionTreeClassifier()


# # As a correct method we should split the dataset into train and test set,but here i am directly applying the data

# In[74]:


Dte.fit(input,target)


# In[75]:


Dte.score(input,target)


# In[77]:


Dte.predict([[3,22,7,1]])


# In[ ]:




