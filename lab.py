price = 1350
quantity = 11
tax_rate = 0.015
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print("Price of item:  $", price)
print("Quantity: ", quantity)
print("Tax Rate: ", tax_rate)

print("Subtotal: $", subtotal)
print("Tax: $", tax)
print("Total: $", total)