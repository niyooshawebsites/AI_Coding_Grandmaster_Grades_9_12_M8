# Parent Class
class Polygon:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        print("Area calculation method of Polygon class")


# Child Class - Rectangle
class Rectangle(Polygon):
    
    def area(self):
        result = self.length * self.breadth
        print("Area of Rectangle:", result)


# Child Class - Square
class Square(Polygon):
    
    def __init__(self, side):
        # Calling parent constructor
        super().__init__(side, side)
    
    def area(self):
        result = self.length * self.breadth
        print("Area of Square:", result)


# Creating Objects
rect = Rectangle(10, 5)
sq = Square(4)

# Calling area methods
rect.area()
sq.area()