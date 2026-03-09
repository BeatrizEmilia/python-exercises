# Program that converts meters to centimeters and millimeters

metros = float(input('Quantos metros? '))

centimetros = metros * 100
milimetros = metros * 1000

print('A medida de {} m corresponde a {} cm e {} mm.'.format(metros, centimetros, milimetros))
