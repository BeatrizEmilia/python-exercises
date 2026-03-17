#022 Create a program that reads a person's full name and displays:
#The name in all CAPITAL LETTERS #The name in all lowercase letters
#Total number of letters (excluding spaces)
#The number of letters in the first name.

nome = str(input('Digite seu nome completo:')).strip()
print(f'Analisando seu nome...')
print(f'Seu nome em maíuscula: {nome.upper()}')
print(f'Seu nome em minuscula: {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
