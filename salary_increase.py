# Salary Increase Calculator
# This program reads an employee's salary and calculates the new salary
# after a 15% increase.

# User input
salary = float(input("Enter the employee's salary R$ / Qual é o salário do funcionário? R$: "))

# Salary calculation
new_salary = salary + (salary * 15 / 100)

# Display result
print(f'New salary: R$ {new_salary:.2f} / Novo salário: R$ {new_salary:.2f}')
