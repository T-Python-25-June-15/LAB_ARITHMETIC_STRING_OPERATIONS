price = 2.99
quantity = 3
tax_rate = 0.075
subtotal = price * quantity
tax = round(subtotal * tax_rate, 2)
total = round(subtotal + tax, 2)
print(f"Price of item: ${price}  Quantity: {quantity} Tax rate: ${tax_rate*100}%  Subtotal: ${subtotal}  Tax: ${tax}  Total: ${total}")



#Bonus

sentence = "We will go home at the end of the day"
word = "the"
print(len(sentence))
print(sentence.index(word))
print(sentence.count(word))
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(word, "replaced"))
print(sentence[-1])