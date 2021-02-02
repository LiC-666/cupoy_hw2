#!/usr/bin/env python
# coding: utf-8

# 作業目標
# 熟悉陣列維度轉換，並且會擷取需要資料
# 作業重點
# 使用reshap須注意order用法
# where可以運用邏輯條件擷取資料
# 
# 題目:
# 1.將下列陣列(array1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")

# In[1]:


import numpy as np


# #1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
# array1 = np.array(range(30))

# In[20]:


a = np.array(range(30))
a


# In[21]:


a.ravel(order='F')


# In[22]:


a.reshape(5,6)


# #2.呈上題的array，找出被6除餘1的數的索引

# In[32]:


np.where( a%7<1)


# In[ ]:




