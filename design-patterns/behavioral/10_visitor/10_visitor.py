from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass
    
    @abstractmethod
    def visit_square(self, square):
        pass

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def accept(self, visitor):
        return visitor.visit_circle(self)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def accept(self, visitor):
        return visitor.visit_square(self)

class AreaCalculator(Visitor):
    def visit_circle(self, circle):
        return 3.14 * circle.radius ** 2
    
    def visit_square(self, square):
        return square.side ** 2

# Usage
shapes = [Circle(5), Square(4)]
calculator = AreaCalculator()
for shape in shapes:
    print(f"Area: {shape.accept(calculator)}")