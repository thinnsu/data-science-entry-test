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
    return lst

#print(lst)

lst = ["apple", "banana", "cherry", "orange", "cherry"]
rst = findandreplace(lst, "orange", "kiwi")
print (rst)
# In[107]:

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


# In[108]:
# Task 2

lst2 = [1, 2, 3, 4, 2, 2]
rst2 = findandreplace(lst2, 2, 5)   
print (rst2)
