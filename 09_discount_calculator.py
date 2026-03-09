# Discount Calculator
# This program reads the price of a product and calculates the new price
# after a 5% discount.

# User input 
product_price = float(input('Enter the product price R$ / Digite o valor do produto R$: '))

# Discount calculation
discounted_price = product_price - (product_price * 5 / 100)

# Display result
print(f'Price after 5% discount: R$ {discounted_price:.2f} / '
      f'Com 5% de desconto: R$ {discounted_price:.2f}')
