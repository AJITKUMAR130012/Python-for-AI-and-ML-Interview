#!/usr/bin/env python
# coding: utf-8

# In[20]:


from itertools import permutations
from itertools import combinations


# In[21]:


a=[1,2,3]


# In[22]:


p=permutations(a,2)


# In[23]:


for i in p:
    print(i,end=" ")


# In[24]:


c=combinations(a,2)


# In[25]:


for i in c:
    print(i)


# In[ ]:




