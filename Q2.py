#!/usr/bin/env python
# coding: utf-8



# In[105]:


#    """
#    Task 1
#   - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
#    - lst must be a list.
#    - Return the modified list.
#    """



def findandreplace(lst, oldVal, newVal):
    for i in range(len(lst)):
        if lst[i] == oldVal:
            lst[i] = newVal

print(lst)

lst = ["apple", "banana", "cherry", "orange", "cherry"]
findandreplace(lst, "orange", "kiwi")



# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


# In[108]:


def findandreplace(lst, oldVal, newVal):
    for i in range(len(lst)):
        if lst[i] == oldVal:
            lst[i] = newVal

print(lst)

lst = [1, 2, 3, 4, 2, 2]
findandreplace(lst, 2, 5)





