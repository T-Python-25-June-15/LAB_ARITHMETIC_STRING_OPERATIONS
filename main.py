price=2.95
quantity=3
tax_rate=0.075
sub_total=price*quantity
tax=sub_total*tax_rate
total=sub_total+tax
print(f"price of items: ${price:.2f}")
print(f"quantity: {quantity}")
print(f"tax_rate: {tax_rate*100}%")
print(f"sub_total: ${sub_total:.2f}")
print(f"tax: ${tax:.2f}")
print(f"total: ${total:.2f}")