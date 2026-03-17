#Create a program that reads a sentence and shows:
#How many times the letter "A" appears
#The position of the first occurrence
#The position of the last occurrence

sentence = input('Enter a sentence: ').strip().upper()

print('The letter A appears {} times'.format(sentence.count('A')))
print('The first occurrence is at position {}'.format(sentence.find('A') + 1))
print('The last occurrence is at position {}'.format(sentence.rfind('A') + 1))
