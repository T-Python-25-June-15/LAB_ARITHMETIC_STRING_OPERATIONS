price:float = 2.99
quantity:int = 3
tax_rate:float = 7.5 # 0.075

subtotal = price * quantity
tax = subtotal * (tax_rate / 100)

total = subtotal + tax

print(f"Price of item: ${price}\nQuanttity: {quantity}\nTax rate: {tax_rate}$\n")
print(f"Subtotal: ${subtotal}\nTax: ${round(tax, 2)}\nTotal: ${round(total, 2)}")