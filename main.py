price:float = 2.99
quantity:int = 3
tax_rate:float =15.0

subtotal= (price * quantity)

tax = round((subtotal * (tax_rate/100)))


total = subtotal + tax

print("price of item: $" + str(price))
print("Quantity: " + str(quantity))
print("Tax rate: " + str(tax_rate) + "%")


print("Subtotal: $" + str(subtotal))
print("Tax: $" + str(tax))
print("Total: $" + str(total))