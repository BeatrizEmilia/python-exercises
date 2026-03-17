#Create a program that reads the name of a city and checks whether it starts with "SANTO".
cidade = str(input('Enter the city name: ')).strip()

print(cidade[:5].upper() == 'SANTO')
