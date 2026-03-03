# Parent Class
class Polygon:
    
    def area(self):
        # This method will be overridden by child classes
        pass


# Child Class - Rectangle
class Rectangle(Polygon):
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth


# Child Class - Square
class Square(Polygon):
    
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side


# Creating objects
rect = Rectangle(12, 6)
sq = Square(5)

# Printing area
print("Area of Rectangle:", rect.area())
print("Area of Square:", sq.area())