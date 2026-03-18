#Create a program that reads a person's full name and displays the first and last name separately.
#Example:
#Input: Ana Maria de Souza
#Output:
#First name: Ana
#Last name: Souza

name = input('Enter your full name: ').strip()

print(f'First name: {name.split()[0]}')
print(f'Last name: {name.split()[-1]}')

strip()
→ Removes extra spaces at the beginning and end

split()
→ Splits the full name into a list of words

[0]
→ Gets the first element (first name)

[-1]
→ Gets the last element (last name)
