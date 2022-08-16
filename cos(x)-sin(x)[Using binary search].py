#!/usr/bin/env python
# coding: utf-8

# # Solution of equation cos(x)-sin(x) 

# In[2]:


import math
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


a=[]


# In[4]:


for i in np.arange(-2,2,0.01):
    a.append(math.cos(i)-math.sin(i))


# In[5]:


for i in a:
    print(i,end=" ")


# In[6]:


b=[]
for i in np.arange(-2,2,0.01):
    b.append(i)


# In[7]:


plt.plot(b,a)
plt.ylabel("cos(x)-sin(x)")
plt.xlabel("x")
plt.show()


# In[9]:


x_s=0
x_e=1
mid=0
y=math.cos(0)-math.sin(0)
while abs(y)>0.001:
    mid=(x_s+x_e)/2
    y=(math.cos(mid)-math.sin(mid))
    if y>0:
        x_s=mid
    if y<0:
        x_e=mid
    


# In[10]:


print(mid)
print(math.cos(mid)-math.sin(mid))


# # Solution of give below f(x)

# In[46]:


def f(x):
    return pow(x,5)-pow(x,4)+(2*pow(x,3))-pow(x,2)+x-3


# In[73]:


a1=[]
b1=[]


# In[74]:


for i in np.arange(-4,6,0.001):
    a1.append(f(i))
    b1.append(i)


# In[75]:


f(4)


# In[76]:


plt.plot(b1,a1)
plt.xlabel("x")
plt.plot("f(x)")
plt.show()


# In[97]:


#linear search


# In[86]:


ans=0
for i in np.arange(-10,10,0.00001):
    if abs(f(i))<0.001:
        ans=i
        break
        


# In[88]:


print(ans)


# In[98]:


#binary search


# In[95]:


s=-4
e=6
mid=(s+e)/2
y=abs(f(mid))
while abs(y)>0.000001:
    mid=(s+e)/2
    y=f(mid)
    if f(mid)>0:
        e=mid
    if f(mid)<0:
        s=mid


# In[96]:


print(mid)


# In[ ]:




