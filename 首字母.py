#!/usr/bin/env python
# coding: utf-8

# In[2]:


def normalize(name):
    name=name[0].upper()+name[1:].lower()
    return name
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)


# In[4]:


def normalize(name):
    return name.capitalize()
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)


# In[ ]:




