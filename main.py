price = 2.99
quantity = 3 
tax_rate = 0.075
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"${subtotal:.2f}")
print(f"${tax:.2f}")
print(f"${total:.2f}")
