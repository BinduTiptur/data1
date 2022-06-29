#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
arr1 = np.array([1,2,3])
print(arr1)


# In[3]:


arr1[2]


# In[4]:


arr1[2]= 5
arr1


# 

# In[7]:


arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)


# In[9]:


print("the shap is 2 rows and 3 columns:", arr2.shape)


# In[11]:


print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1, 0])


# In[12]:


arr3 = np.array(['india', 'china', 'usa', 'mexico'])
print(arr3)


# In[13]:


arr3[1]


# In[15]:


arr = np.arange(0, 20, 2)
print(arr)


# In[16]:


arr = np.linspace(0, 10, 20)
print(arr)


# In[21]:


arr = np.random.rand(10)
print(arr)
print('\n')
arr = np.random.rand(3,4)
print(arr)


# In[22]:


print(np.full((4,6),10))


# In[23]:


arr = [0, 1, 2]
print(np.repeat(arr, 3))


# In[24]:


arr = [0, 1, 2]
print(np.repeat(arr, 3))


# In[25]:


arr = [0, 1, 2]
print(np.tile(arr, 3))


# In[26]:


identity_matrix = np.eye(3)
print(identity_matrix)


# In[28]:


identity_matrix = np.identity(3)
print(identity_matrix)


# In[29]:


arr = np.random.rand(5,5)
print(arr)


# In[30]:


print(np.sum(arr, axis=0))


# In[31]:


print(np.sum(arr, axis=1))


# In[32]:


print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[33]:


arr = np.random.rand(5,5)
print(arr)


# In[34]:


print(np.sort(arr, axis=1))


# In[35]:


arr = np.array([4,5,6,7])
arr1 = np.append(arr, 8)
arr1


# In[36]:


arr2 = np.append(arr, [9,10,11])
print(arr2)


# In[37]:


arr2 = np.array([4,5,6,7,9,10,11])
print(arr2)
print('\n')
arr5 = np.delete(arr2, [1,4])
print(arr5)


# In[38]:


arr1 = np.array([[1,2,3,4], [1,2,3,4]])
arr2 = np.array([[5,6,7,8], [5,6,7,8]])
cat = np.concatenate((arr1, arr2), axis=0)
print(cat)


# In[39]:


cat =np.concatenate((arr1, arr2), axis=1)
print(cat)

