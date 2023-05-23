#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[9]:


array1=[23,45,18]
num=np.array(array1)
print(num)


# In[15]:


np.random.rand(2,3)


# In[16]:


np.random.random(size=2)


# In[19]:


np.random.randint(1,101,100)


# # 

# In[24]:


np.arange(1,10,5)


# In[28]:


np.arange(0,50,5)


# In[29]:


np.arange(100,0,-1)


# In[32]:


np.linspace(0,1,6)


# In[37]:


np.zeros(10,int)


# In[38]:


np.ones(100,int)


# In[41]:


matrix=np.empty((3,3),int)
print(matrix)


# In[43]:


matrix=np.full((3,3),10)
print(matrix)


# In[44]:


np.identity(50)


# In[56]:


arr=np.arange(2,21)
print(arr)


# In[57]:


sample_array=np.arange(2,10)
print(sample_array[4])


# In[ ]:




