subtotal = eval(input("Enter the subtotal: $"))
tipp = eval(input("Enter tip amount (as a %): "))

tip = (tipp/100)*subtotal
total = subtotal + tip

print("")
print("------------------------")
print("Subtotal: ${:,.2f}".format(subtotal))
print("Tip : ${:,.2f}".format(tip))
print("Total : ${:,.2f}".format(total))
print("------------------------")
print("")