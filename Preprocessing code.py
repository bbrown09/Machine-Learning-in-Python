#!/usr/bin/env python
# coding: utf-8

# In[7]:


def keep_numeric_columns(df):
    return df.select_dtypes(include=['number'])


# In[8]:


# Reading in training data
delays = pd.read_csv('train_data.csv')
delays = delays.dropna()
delays = keep_numeric_columns(delays)


# In[ ]:


# Reading in test data
new_data = pd.read_csv('new_data.csv')
new_data = new_data.dropna()
new_data = keep_numeric_columns(new_data)


# In[ ]:


# Creating Features and Target variables
y = delays['DEP_DEL15']
X = delays.drop('DEP_DEL15', axis=1)

