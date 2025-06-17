# Luluh Almogbil 

price, Quantity, tax_rate = 2.99, 3, 7.5

#calculate subtotal 
subtotal = price*Quantity

#calculate tax 
tax = subtotal*(tax_rate/100)

#calculate total cost 
total = subtotal+tax

print("Price of item: $",price,"\nQuantity: ",Quantity,"\nTax rate: ",tax_rate,"%")
print ("\nSubtotal: $",subtotal,"\nTax: $",round(tax,2),"\nTotal: $",round(total,2))



