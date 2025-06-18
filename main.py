#1. Define a variable named 
# "price" and set its value to the cost of the item the customer is purchasing (e.g., $2.99).

price =13
quantity=4
tax_rate=0.15 #15% tax

subtotal= price * quantity

tax= subtotal * tax_rate

total= subtotal + tax 

print("Price of item: $" + str(price))
print("Quantity:",quantity)
print("Tax rate: {}%".format(tax_rate*100))

print()
print("Subtotal:{}$" .format(subtotal))
print("Tax:{}$" .format(tax))
print("Total:{}$" .format(total))