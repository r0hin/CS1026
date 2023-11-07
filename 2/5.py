import math

rectwidth = input("What is the width of the rectangle? ")
rectheight = input("What is the height of the rectangle? ")
print("The area of the rectangle is " + str(int(rectwidth) * int(rectheight)) + ".");

trianglewidth = input("What is the width of the triangle? ")
triangleheight = input("What is the height of the triangle? ")
print("The area of the triangle is " + str(int(trianglewidth) * int(triangleheight) / 2) + ".");

circleradius = input("What is the radius of the circle? ")
print("The area of the circle is " + str(int(circleradius) * int(circleradius) * math.pi) + ".");