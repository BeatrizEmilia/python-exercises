Create a program that reads the length of the opposite leg and the adjacent leg of a right triangle and calculates the hypotenuse.

from math import sqrt

co = float(input('Length of the opposite leg: '))
ca = float(input('Length of the adjacent leg: '))

hypotenuse = sqrt(co ** 2 + ca ** 2)

print(f'The length of the hypotenuse is {hypotenuse:.2f}')
-------------------------------------------------------------
import math

co = float(input('Length of the opposite leg: '))
ca = float(input('Length of the adjacent leg: '))

hi = math.hypot(co, ca)

print(f'The hypotenuse will measure {hi:.2f}')
