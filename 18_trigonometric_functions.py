#Create a program that reads any angle and displays the sine, cosine, and tangent of that angle.

import math

angle = float(input('Enter the angle value: '))

sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print(f'Sine: {sine:.2f}')
print(f'Cosine: {cosine:.2f}')
print(f'Tangent: {tangent:.2f}')
