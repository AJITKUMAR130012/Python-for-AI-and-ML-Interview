#!/usr/bin/env python
# coding: utf-8

# In[124]:


import math
import numpy as np
import matplotlib.pyplot as plt


# In[125]:


a=[]


# In[126]:


b=np.arange(0,4,0.01)


# In[127]:


for x in np.arange(0,4,0.01):
    a.append(math.sin(x)-math.cos(x))


# In[128]:


plt.plot(b,a)
plt.ylabel("sin(x)-cos(x)")
plt.xlabel("x")
plt.show()


# In[129]:


for x in np.arange(0,3,0.000001):
    if math.sin(x)-math.cos(x)<0:
        a=x
    if math.sin(x)-math.cos(x)>0:
        b=x
        break;
        


# In[130]:


print(a,b)


# In[131]:


ans=(a+b)/2


# In[132]:


print(ans)


# In[134]:


math.sin(ans)-math.cos(ans)


# In[ ]:




