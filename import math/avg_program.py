from math import sqrt, pow
a, b = float(input()), float(input())
middle_arith = (a + b) / 2
middle_geom = sqrt(a * b)
middle_garmoni = (2 * a * b) / (a + b)
middle_square = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(middle_arith, middle_geom, middle_garmoni, middle_square, sep='\n')
