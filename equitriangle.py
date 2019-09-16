"""
equitriangle.py
Date: 9/5/2019
Author: David T.

description...
	
"""

side1 = int(input("Enter side 1 of the triangle: "))
side2 = int(input("Enter side 2 of the triangle: "))
side3 = int(input("Enter side 3 of the triangle: "))

if side1 == side2 == side3:
	print("Your triangle is equilateral.")
else:
	print("Your triangle is NOT equilateral.")

input()