import math


# Function to calculate the area of a rectangle
def rectangle_area(length, width):
  return length * width


# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
  return 2 * (length + width)


# Function to calculate the area of a square
def square_area(side):
  return side**2


# Function to calculate the perimeter of a square
def square_perimeter(side):
  return 4 * side


# Function to calculate the area of a circle
def circle_area(radius):
  return math.pi * radius**2


# Function to calculate the circumference of a circle
def circle_circumference(radius):
  return 2 * math.pi * radius


# Function to calculate the area of a triangle
def triangle_area(base, height):
  return 0.5 * base * height


# Function to calculate the perimeter of a triangle
def triangle_perimeter(side1, side2, side3):
  return side1 + side2 + side3


# Function to calculate the area of a parallelogram
def parallelogram_area(base, height):
  return base * height


# Function to calculate the perimeter of a parallelogram
def parallelogram_perimeter(side1, side2):
  return 2 * (side1 + side2)


# Function to calculate the area of a trapezoid
def trapezoid_area(base1, base2, height):
  return 0.5 * (base1 + base2) * height


# Function to calculate the perimeter of a trapezoid
def trapezoid_perimeter(side1, side2, base1, base2):
  return side1 + side2 + base1 + base2
