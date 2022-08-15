#!/usr/bin/env python
# coding: utf-8

# In[33]:


import math


# In[34]:


(cx,cy,r)=(input().split(' '))


# In[35]:


print(cx,cy,r)


# In[36]:


cx=int(cx)
cy=int(cy)
r=int(r)


# In[37]:


(p,q)=input().split(' ')


# In[38]:


p=int(p)
q=int(q)


# In[39]:


z=math.sqrt((p-cx)**2 +(q-cy)**2)


# In[40]:


print(z)


# In[41]:


if z==r:
    print("point on the circle")
if z>r:
    print("Point outside the circle")
if z<r:
    print("Point inside the circle")


# In[ ]:




