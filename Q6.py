#!/usr/bin/env python
# coding: utf-8

# In[6]:


def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """

    i = 0
    while i < len(lst):
        print(lst[i])
        if lst[i] < 0:
            print("The number is negative")
            break
        i += 1
    else:
        print("No negatives")

    return


lst = [3, 5, -1, 7, -2, 8]
find_first_negative(lst)


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]


# In[7]:


lst = [2, 10, 7, 0]

find_first_negative(lst)


# In[ ]:
