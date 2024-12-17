"""
A class for representing a circle
"""

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.pie = 3.14
    
    def calculate_circumference(self):
        print(f"Circumference: {2 * self.pie * self.radius} units")

    def calculate_area(self):
        print(f"Area: {self.pie * (self.radius ** 2) } square units")

new_circle = Circle(2)

new_circle.calculate_circumference()
new_circle.calculate_area()
