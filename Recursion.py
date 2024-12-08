#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_factorial(n):
    fact = 1
    if n<0:
        return "Number cannot be negative"

    else:
        for i in range(1,n+1):
            fact*=i
        return fact
    
get_factorial(5)


# In[5]:


def fibonacci(n):
    if n<0:
        return "Please enter a positive number"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(n=int(input("Please enter a number:"))))


# In[ ]:




