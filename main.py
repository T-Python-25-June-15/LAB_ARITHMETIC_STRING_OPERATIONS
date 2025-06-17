price = 2.99
quantity = 3 
tax_rate = 0.075
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Price of item: ${price:.2f}")
print(f"Quantity: ${quantity:.2f}")
print("Tax rate: 7.5% \n")
print(f"Subtotal: ${subtotal:.2f}")
print(f"tax: ${tax:.2f}")
print(f"total: ${total:.2f}")
