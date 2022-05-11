#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


customer_data = pd.read_csv('Wholesale customers data.csv')
data = customer_data.iloc[:, 4:6].values


labels = range(1, 11)
plt.figure(figsize=(10, 8))
plt.subplots_adjust(bottom=0.1)
plt.scatter(data[:,0],data[:,1], label='True Position')
plt.xlabel=('milk')
plt.ylabel=('grocery')

plt.show()


# In[ ]:





# In[12]:


import scipy.cluster.hierarchy as shc

plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward'))


# In[ ]:




