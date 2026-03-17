#Problem
#Create a program that reads a number from 0 to 9999 and displays each digit separately:
#Example:
#Input: 1834
#Output:
#Units: 4
#Tens: 3
#Hundreds: 8
#Thousands: 1

num = int(input('Enter a number: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'The number entered was {num}.')
print(f'Units: {unidade}')
print(f'Tens: {dezena}')
print(f'Hundreds: {centena}')
print(f'Thousands: {milhar}')
