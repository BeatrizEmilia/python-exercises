#Program that displays the multiplication table of a number

numero = int(input('Digite um número para ver sua tabuada: '))

print('--' * 12)

for c in range(1, 11):
    print(f'{numero} x {c:2} = {numero * c}')

print('--' * 12)
