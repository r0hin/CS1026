class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __add__(self, other):
        # Overload the '+' operator to add two Point objects
        return Point(self.x + other.x, self.y + other.y)
         
 
    def __str__(self):
        return f"Point({self.x}, {self.y})"
 
# Create two Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)
 
# Use the overloaded '+' operator to add points
result = point1 + point2
 
# Print the results
print(f"point1: {point1}")
print(f"point2: {point2}")
print(f"point1 + point2: {result}")