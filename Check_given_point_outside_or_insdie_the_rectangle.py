#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[3]:


(x1,y1,x2,y2)=input().split(' ')


# In[4]:


x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)


# In[5]:


(p,q)=input().split(' ')


# In[7]:


p=int(p)
q=int(q)


# In[8]:


if p>x1 and p<x2 and q>y1 and q<y2:
    print("Point lies inside the rectanle")
else:
    print("Point lies outside the rectangle")


# In[ ]:




