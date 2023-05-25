#!/usr/bin/env python
# coding: utf-8

# ## Programming Assignment_1
# -------------

# ### 1. Write a Python program to print "Hello Python"?
# ##### Sol:

# In[1]:


print("Hello Python")


# ### 2. Write a Python program to do arithmetical operations addition and division.?
# ##### Sol:

# In[24]:


a = 10
b = 2

## Addition
add = a + b
## Division
div = a/b

print(add)
print(div)


# ### 3. Write a Python program to find the area of a triangle?
# ##### Sol:

# In[6]:


height = 100
base = 25

area = height*base/2

print("Area of triangle:", area)


# ### 4. Write a Python program to swap two variables?
# ##### Sol:

# In[11]:


var1 = 123
var2 = 111

print('Before swap:\nvar1 = {} and var2 = {}'.format(var1, var2))

temp = var1
var1 = var2
var2 = temp
print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))


# ### 5. Write a Python program to generate a random number?
# ##### Sol:

# In[23]:


import random

print(random.random())
print(random.randint(1, 1000))


# In[ ]:




