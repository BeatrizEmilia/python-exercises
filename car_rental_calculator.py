# Car Rental Calculator
# This program calculates the total cost of renting a car based on
# the number of days rented and kilometers driven.

# User input
days = int(input('Quantos dias alugados? '))
km_driven = float(input('Quantos km rodados? '))

# Total cost calculation 
total_payment = (days * 60) + (km_driven * 0.15)

# Display result 
print(f'Total to pay: R$ {total_payment:.2f})
