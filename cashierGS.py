#you can play with this numbers or changing it
price = 2.99
quantity = 3
tax_rate = 7.5

#thats loop will ask you if you want to try again with enter the number from console
while True:
    subtotal = price * quantity
    tax = subtotal * (tax_rate / 100)
    total = subtotal + tax

    print(f"""
        ###############################
        
        Price of Item: ${price}
        Quantity: {quantity}
        Tax rate: {tax_rate}% 

        Subtotal: ${subtotal}
        Tax: ${tax:.2f}
        Total: ${total:.2f}

        ###############################
    """)

    option = input("Would you like to Enter the number manually? (y for yes, n for no): ")

    #if you enter y or Y it will allow you to enter the numbers

    if option == "y" or option == "Y":
        price = input("Price: $")
        quantity = input("Quantity: ")
        tax_rate = input("Tax_rate(example 7.5): ")
        
        price = float(price)
        quantity = int(quantity)
        tax_rate = float(tax_rate)
    else:
        print("Closing...")
        break