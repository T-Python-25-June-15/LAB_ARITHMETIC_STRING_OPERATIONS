
price , quantity , tax_rate = 2.99 , 3 , 7.5

subtotal = price * quantity
tax = (subtotal * tax_rate)/100
total = subtotal + tax

print(f"Price of item: {price}$")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")

print(f"Subtotal: {subtotal}$")
print(f"Tax: {round(tax,2)}$")
print(f"Total: {round(total,2)}$")