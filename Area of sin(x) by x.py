#!/usr/bin/env python
# coding: utf-8

# # Compute the area under sin(x)/x

# In[9]:


import matplotlib.pyplot as plt
import math
import numpy as np


# In[42]:


def fun(x):
    if x==0:
        return 0
    else:
        return abs(math.sin(x)/x)


# In[43]:


ans=0
for i in np.arange(-10,10,0.1):
    ans+=((fun(i))*0.1)


# In[44]:


print(ans)


# # Find the maxima f(x)=sin(x)/x in [-2,2]

# In[45]:


def realfun(x):
    if x==0:
        return 1
    else:
        return (math.sin(x)/x);
    
def slop(x):
    delta=0.01
    return (realfun(x+delta)-realfun(x))/delta


# In[46]:


array1=[]
array2=[]
for i in np.arange(-2,5,0.01):
    array1.append(i)
    array2.append(slop(i))


# In[47]:


plt.plot(array1,array2)
plt.show()


# In[48]:


s=-2
e=5
mid=(s+e)/2
while(abs(slop(mid))>0.01):
      mid=(s+e)/2
      y=slop(mid)
      if y>0:
          s=mid
      if y<0:
          e=mid
      


# In[49]:


print(mid)


# 
# # find the maxima for equation x^2+sin(x)+2*x

# In[50]:


def polynomial(x):
    return pow(x,2)+math.sin(x)+2*x
def slop_pol(x):
    delta=0.01
    return (polynomial(x+delta)-polynomial(x))/delta


# In[51]:


listX=[]
listY=[]
listx=[]
listy=[]


# In[52]:


for i in np.arange(-5,5,0.01):
    listX.append(i)
    listx.append(i)
    listY.append(polynomial(i))
    listy.append(slop_pol(i))


# In[53]:


plt.plot(listX,listY)
plt.show()


# In[54]:


plt.plot(listx,listy)
plt.show()


# In[55]:


polynomial(-2)


# In[56]:


slop_pol(0)


# In[57]:


start=-4
end=4
mid=(start+end)/2
y=slop_pol(mid)
while (abs(y)>0.01):
    mid=(start+end)/2
    y=slop_pol(mid)
    if y>0:
        end=mid
    if y<0:
        start=mid
        


# In[58]:


print(mid)


# In[62]:


print(slop_pol(mid))


# # Find if circle intersect at one point or not

# In[67]:


(c1,c2,r1)=input().split(' ')
c1=int(c1)
c2=int(c2)
r1=int(r1)


# In[76]:


print(c1,c2,r1)


# In[73]:


(c3,c4,r2)=input().split(' ')
c3=int(c3)
c4=int(c4)
r2=int(r2)


# In[74]:


print(c3,c4,r2)


# In[78]:


d=math.sqrt(pow(c1-c3,2)+pow(c2-c4,2))


# In[79]:


print(d)


# In[80]:


if d==r1+r2:
    print("circle are orthogonal")
if d>r1+r2:
    print("Both circle are do not intersect")
if d<r1+r2:
    print("Both circle are intersect to each other")


# # find the factorial of large number

# In[120]:


n=int(input())
ans=[]
#initially this list store the factorial for n==1
ans.append(1)
#this loop is executed for i=2 to n
for i in range(2,n+1,1):
    c=0
    #list contain every number in reverese order and multiply with i all time
    for j in range(0,len(ans),1):
        x=ans[j]*i
        ans[j]=(x+c)%10
        c=int((x+c)/10)
        # storing the value of carry
        if j==(len(ans)-1) and c!=0:
            while c!=0:
                ans.append(c%10)
                c=int(c/10)

            


# In[121]:


ans.reverse()
print(ans)


# # Monticarlo Simulation--> value of PI

# In[40]:


n=int(input())


# In[41]:


(cx,cy,r)=input().split(' ')
cx=float(cx)
cy=float(cy)
r=float(r)


# In[42]:


print(cx,cy,r)


# In[43]:


m=0
for i in range(n):
    x=np.random.random()
    y=np.random.random()
  
    d=math.sqrt(pow(cx-x,2)+pow(cy-y,2))
    if d<=r:
        m=m+1


# In[44]:


(4*m)/n


# In[ ]:




