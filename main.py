#lab 1 arithmetic_string operations (wasan alqahtani)


#Define a variable named "price" and set its value to the cost of the item the customer is purchasing
price = 2.99

#Define a variable named "quantity" and set its value to the number of items the customer is purchasing
quantity = 3

#Define a variable named "tax_rate" and set its value to the tax rate in your area
tax_rate = 7.5

#Calculate the subtotal by multiplying the price by the quantity and store the result in a variable named "subtotal".
subtotal = price * quantity

#Calculate the tax by multiplying the subtotal by the tax rate (in decimal form) and store the result in a variable named "tax".
tax = subtotal * (tax_rate/100)

#Calculate the total cost by adding the subtotal and the tax, and store the result in a variable named "total".
total = subtotal + tax 

print (f"Price of item: ${price}")
print(f"Quantity: {quantity}")
print(f"Tax rate: {tax_rate}%\n")
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${round(tax,2)}")
print(f"Total: ${round(total,2)}")





