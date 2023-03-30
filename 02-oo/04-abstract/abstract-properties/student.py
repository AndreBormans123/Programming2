import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass
    
    @property
    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length   
        
    @property
    def area(self):
        return self.length * self.width
    
    @property
    def perimeter(self):
        return (self.width + self.length) * 2
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @property
    def area(self):
        return self.width ** 2

    @property
    def perimeter(self):
        return self.width * 4
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    

    
    
    