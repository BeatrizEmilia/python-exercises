#A teacher wants to randomly determine the presentation order of student groups.
Create a program that reads the names of four groups and displays them in a random order.
  
import random

group1 = input('Enter the first group name: ')
group2 = input('Enter the second group name: ')
group3 = input('Enter the third group name: ')
group4 = input('Enter the fourth group name: ')

groups = [group1, group2, group3, group4]

random.shuffle(groups)

print('Presentation order:')
print(f'First group: {groups[0]}')
print(f'Second group: {groups[1]}')
print(f'Third group: {groups[2]}')
print(f'Fourth group: {groups[3]}')
