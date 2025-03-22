# first to implementa abstraction we will need to import abc module
# from there we need specifically ABC and abstractmethod
from abc import ABC, abstractmethod

# then we inherit from ABC
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    # we can have regular methods as well
    def describe(self):
        return f"This is a shape with area {self.area()} and perimeter {self.perimeter()}"


# inherit the class wityh abstraction appied
# implement the abstract methods  
    
from math import pi    
    
# concrete class
# Concrete implementation of the Shape class    
class Circle(Shape):
    
    def __init__(self, radius):
        self.__radius = radius
        
    # implement the abstract methods from Shape class    
    def area(self):
        return pi * self.__radius * self.__radius
    
    def perimeter(self):
        return 2 * pi * self.__radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
         return self.__width * self.__height
     
    def perimeter(self):
        return 2 * (self.__width + self.__height)    
          

circle = Circle(5)
rectangle = Rectangle(10, 15)

print(circle.perimeter())
print(circle.area())
print(circle.describe())


print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.describe())

