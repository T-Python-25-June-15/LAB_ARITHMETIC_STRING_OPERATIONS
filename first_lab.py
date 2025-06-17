price=float(input("Enter the price of Item:"))
quantity=int(input("Enter the auantity:"))
task_rate_percentage=float(input("Enter the task_rate(%):"))

task_rate=task_rate_percentage/100


subtotla= price*quantity
task= subtotla * task_rate
total= subtotla + task

print("\n Receipt")
print("price: ${:.2f}".format(price))
print("quantity: {}".format(quantity))
print("task rate:{:.1f}%".format(task_rate_percentage))

print("\n")
subtotal = price * quantity     


print("Subtotal: ${:.2f}".format(subtotal)) 
print("Tax: ${:.2f}".format(task))
print("Total: ${:.2f}".format(total))
