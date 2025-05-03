#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    # def describe_car(self, year, make, model):
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")



# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020


# In[13]:


c1 = Car("2020", "Toyota", "Corolla")

describe_car = c1.describe_car()


# In[ ]:
