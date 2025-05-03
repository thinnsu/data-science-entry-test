#!/usr/bin/env python
# coding: utf-8

# In[50]:


#   Task 1
#   - Create a function that would swap the value of x and y using only x and y as variables.
#   - x and y must be numeric.
#   - Return -1 if x and y is not numeric, and
#   - print the swapped values if both x and y are numeric.
#   """
def swap(x, y):   
   if (x.isnumeric()== False or y.isnumeric()== False):
       print ("-1")
   else:
       x, y = y, x  # swapping

       print("x:", x)
       print("y:", y)

   return


swap("28", "5")


# In[47]:


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
def swap(x, y):

    x, y = y, x  # swapping

    print("x:", x)
    print("y:", y)
    return

swap("Apple", 10)





