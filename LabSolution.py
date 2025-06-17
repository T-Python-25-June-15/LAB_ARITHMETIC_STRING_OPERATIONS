price:float = 2.99
quantity:int = 3
tax_rate:float = 7.5
subtotal:float = price * quantity
tax:float = subtotal * (tax_rate/100)
total:float = subtotal + tax

print(f"""   
Price of item: ${price}
Quantity: {quantity}
Tax rate: {tax_rate}%

Subtotal: ${subtotal}
Tax: ${round(tax, 2)}
Total: ${round(total, 2)}
""")