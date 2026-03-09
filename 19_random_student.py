#A teacher wants to randomly choose one of four students to erase the board.
Create a program that reads the names of four students and randomly selects one.

import random

student1 = input('Enter the first student name: ')
student2 = input('Enter the second student name: ')
student3 = input('Enter the third student name: ')
student4 = input('Enter the fourth student name: ')

students = [student1, student2, student3, student4]

chosen = random.choice(students)

print(f'The chosen student is {chosen}.')
