Create a program that reads a real number from the keyboard and displays only the integer part of that number on the screen.
Example:
Enter a number: 6.127
The number 6.127 has the integer part 6

num = float(input('Enter a number: '))
integer = int(num)

print(f'The number {num} has the integer part {integer}')
------------------------------------------------------------
from math import trunc

num = float(input('Enter a number: '))
integer = trunc(num)

print('The number entered was {} and its integer part is {}'.format(num, integer))
