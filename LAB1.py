Price = 2.99
Quantity = 3
Tax_rate = 7.5

Subtotal = Price * Quantity
Tax =  Subtotal * 0.075
Total = Subtotal + Tax
rounded_Tax = round(Tax, 2)
rounded_Total = round(Total, 2)



print (str(Subtotal) +"$")
print (str(rounded_Tax) +"$")
print(str(rounded_Total) +"$")
