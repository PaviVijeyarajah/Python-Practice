#!/usr/bin/env python
# coding: utf-8

# In[10]:


class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)


# In[2]:


def no_return():
    print("I am about to raise an exeception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

def call_exceptor():
    print("call_exceptor starts here ...")
    no_return()
    print("An exception was raised...")
    print(" ... so these lines don't run")
call_exceptor()  


# In[3]:


def no_return():
    print("I am about to raise an exeception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

try:
    no_return()
except: 
    print("I caught an exception")

print("Executed after except")


# In[ ]:


try: 
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print("x/y = ", x/y)
    print("x*y = ", x*y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid value is entered")
except: 
    print("Something went wrong")


# In[ ]:


class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):
        return "color: " + self.__color +             " and filled: " + str(self.__filled)


# In[ ]:


from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return self.__radius * self.__radius * math.pi
  
    def getDiameter(self):
        return 2 * self.__radius
  
    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def printCircle(self):
        print(self.__str__() + " radius: " + str(self.__radius))


# In[ ]:


def main():
    circle = Circle(1.5)
    print("A circle", circle)
    print("The radius is", circle.getRadius())
    print("The area is", circle.getArea())
    print("The diameter is", circle.getDiameter())
main() # Call the main function


# In[ ]:




