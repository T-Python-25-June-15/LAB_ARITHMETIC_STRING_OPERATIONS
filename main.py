# Define a variables
price = 2.99
quantity = 3
tax_rate = 7.5

print("Price of item:" , f"${price}")
print("Quantity: ", quantity)
print("Tax rate: ", f"%{tax_rate}")

# Calculate the subtotal
subtotal = price * quantity

# Calculate the tax 
tax = subtotal * (tax_rate/100)

# Calculate the total cost
total = subtotal + tax

print("")

#Print the result
print("Subtotal: ", f"${round(subtotal,2)}")
print("Tax: ", f"${round(tax,2)}")
print("Total: " , f"${round(total,2)}")

