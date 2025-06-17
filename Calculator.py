price:float = 2.99
quantity:int = 3
tax_rate:float = 7.5

subtotal:float = price * quantity
tax:float = subtotal * (tax_rate/100)

# Print the receipt details
print(f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${round(tax,2)}")
print(f"Total: ${round(subtotal+tax,2)}")
