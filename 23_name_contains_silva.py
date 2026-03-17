#Create a program that reads a person's full name and checks whether it contains the word "Silva".

nome = str(input('Enter your full name: ').strip())

print('Does your name contain "Silva"? {}'.format('silva' in nome.lower()))
