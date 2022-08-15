#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
a=np.random.random((2,3,3))
print(a)


# In[11]:


b=np.random.random((2,3,3))
print(b)


# In[12]:


c=np.zeros((2,3,3))


# In[13]:


for i in range(0,2):
    for j in range(0,3):
        for k in range(0,3):
            c[i][j][k]=a[i][j][k]+b[i][j][k]


# In[14]:


c


# In[ ]:




