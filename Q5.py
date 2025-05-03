#!/usr/bin/env python
# coding: utf-8

# In[8]:


def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    if (num.isnumeric()== True and divisor.isnumeric()== True):
        print ("True")
    else:
        print ("False")
    return

check_divisibility("10","2")
# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3


# In[9]:


check_divisibility("7","3")


# In[10]:


check_divisibility("str","3")


# In[ ]:




