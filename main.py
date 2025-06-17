
price = 2.99
print("price:$",price)
quantity = 3
print("quantity:",quantity)
tax_rate = (7.5)%(100)
print("tax_rate:",tax_rate,"%")

print()
print()
subtotal = price * quantity
print("subtotal: $",subtotal)
tax = 0.075 * subtotal
print(f"tax: ${tax:.2f}")
total = (subtotal + tax)
print(f"total: ${total:.2f}")