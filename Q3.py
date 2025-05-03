#!/usr/bin/env python
# coding: utf-8


# In[137]:


def update_dictionary(dct1, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    print(dct1)
    dct1.update([(key, value)])
    print(dct1)
    return


dict1 = {"a": 1, "b": 2}

update_dictionary(dict1, "b", 3)

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


# In[141]:


dict1 = {"name": "A", "age": 25}

update_dictionary(dict1, "name", "Alice")
update_dictionary(dict1, "age", 26)


# In[ ]:
